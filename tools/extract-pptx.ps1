# One-time extraction of the China map and six Office line icons from the
# CHBC sales deck pptx. Icon SVGs carry embedded Icons_* ids; each is checked
# against the expected id before it is renamed, so a media reshuffle in the
# pptx fails loudly instead of shipping the wrong icon.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem

$root = Split-Path $PSScriptRoot -Parent
$pptx = 'D:\Final Documents Folder\Job Documents\CHBC\Styling Resources\CHBC Sales Slides.pptx'

New-Item -ItemType Directory -Force (Join-Path $root 'assets\imagery') | Out-Null
New-Item -ItemType Directory -Force (Join-Path $root 'assets\icons')   | Out-Null

$zip = [IO.Compression.ZipFile]::OpenRead($pptx)
try {
    # Map: byte-identical copy, no recompression (flat-colour tier blues must not shift)
    $entry = $zip.GetEntry('ppt/media/image13.png')
    [IO.Compression.ZipFileExtensions]::ExtractToFile($entry, (Join-Path $root 'assets\imagery\map-china-tiers.png'), $true)

    $icons = @(
        @{ media = 'image4.svg';  out = 'bullseye.svg';    id = 'Icons_Bullseye' },
        @{ media = 'image5.svg';  out = 'eye.svg';         id = 'Icons_Eye' },
        @{ media = 'image6.svg';  out = 'calendar.svg';    id = 'Icons_FlipCalendar' },
        @{ media = 'image9.svg';  out = 'server.svg';      id = 'Icons_Server_M' },
        @{ media = 'image10.svg'; out = 'checklist.svg';   id = 'Icons_Checklist_LTR' },
        @{ media = 'image11.svg'; out = 'call-center.svg'; id = 'Icons_CallCenter_M' }
    )
    foreach ($i in $icons) {
        $e = $zip.GetEntry("ppt/media/$($i.media)")
        $reader = New-Object IO.StreamReader($e.Open())
        $svg = $reader.ReadToEnd(); $reader.Close()
        if ($svg -notmatch [regex]::Escape($i.id)) { throw "$($i.media) does not contain expected id $($i.id)" }
        if ($i.out -eq 'call-center.svg') { $svg = $svg -replace '#1976B9', '#0067B1' }
        $svg | Out-File (Join-Path $root "assets\icons\$($i.out)") -Encoding utf8 -NoNewline
        Write-Host "$($i.media) -> $($i.out) [$($i.id)] OK"
    }
} finally { $zip.Dispose() }

Get-ChildItem (Join-Path $root 'assets\imagery'), (Join-Path $root 'assets\icons') | Format-Table Name, Length -AutoSize
