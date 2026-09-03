# One-time extraction of the 24 base64 images embedded in the original
# Gemini-built index.html into real files under assets/, with a manifest
# recording provenance (source caption/alt, bytes, pixel dims, SHA256).
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$root = Split-Path $PSScriptRoot -Parent
$html = Get-Content (Join-Path $root 'index.html') -Raw -Encoding UTF8

New-Item -ItemType Directory -Force (Join-Path $root 'assets\people')  | Out-Null
New-Item -ItemType Directory -Force (Join-Path $root 'assets\clients') | Out-Null

$manifest = @()

function Save-Image([string]$relPath, [string]$b64, [string]$source) {
    $abs = Join-Path $root $relPath
    $bytes = [Convert]::FromBase64String($b64)
    [IO.File]::WriteAllBytes($abs, $bytes)
    $img = [System.Drawing.Image]::FromFile($abs)
    $dims = "$($img.Width)x$($img.Height)"
    $img.Dispose()
    $hash = (Get-FileHash $abs -Algorithm SHA256).Hash
    $script:manifest += [pscustomobject]@{
        file = $relPath; source = $source; bytes = $bytes.Length; dimensions = $dims; sha256 = $hash
    }
}

# Portraits: src precedes alt="Portrait of NAME"
$portraits = [regex]::Matches($html, 'data:image/jpeg;base64,([A-Za-z0-9+/=]+)"\s+alt="Portrait of ([^"]+)"')
foreach ($m in $portraits) {
    $name = $m.Groups[2].Value
    $slug = ($name.ToLower() -replace '[^a-z0-9]+', '-').Trim('-')
    Save-Image "assets\people\$slug.jpg" $m.Groups[1].Value "Portrait of $name"
}

# Client logos: figure > img data URI, figcaption follows
$clients = [regex]::Matches($html, '<figure class="client"><img src="data:image/png;base64,([A-Za-z0-9+/=]+)"[^>]*>\s*<figcaption>([^<]+)</figcaption>')
foreach ($m in $clients) {
    $caption = $m.Groups[2].Value
    $slug = ($caption.ToLower() -replace '&amp;', 'and' -replace '[^a-z0-9]+', '-').Trim('-')
    Save-Image "assets\clients\$slug.png" $m.Groups[1].Value $caption
}

$manifest | ConvertTo-Json | Out-File (Join-Path $PSScriptRoot 'extract-manifest.json') -Encoding utf8

Write-Host "Portraits: $($portraits.Count)  Clients: $($clients.Count)  Total: $($manifest.Count)"
$manifest | Format-Table file, source, bytes, dimensions -AutoSize
