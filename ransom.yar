rule Findyou_HAHA {
    meta:
        author = "henry"
        description = "Detectador de ransom"
        date = "15/09"

    strings:
        $a0 = "icacls"
        $s0 = "kernel32.dll" wide ascii nocase
        $s1 = "advapi32.dll" wide ascii nocase
        $s2 = "user32.dll" wide ascii nocase

    condition:
        any of them
}

rule TESTE_FILE {
    meta:
        description = "file teste"

    strings:
        $s1 = ".java"
        $s2 = ".pdf"
        $s3 = ".mov"
        $s4 = ".zip"
        $s5 = ".mp4"
        $s6 = ".doc"
        $s7 = ".docx"
        $s8 = ".jpg"
        $s9 = ".pptx"
        $s10 = ".mkv"
        $s11 = ".png"
        $s12 = ".txt"
        $s13 = ".iso"
        $s14 = ".mp3"
        $s15 = ".docb"
        $s16 = ".docm"
        $s17 = ".cmd"
        $s18 = ".7z"
        $s19 = ".rar"
        $s20 = ".jpeg"

    condition:
        any of them
}

rule Rule_Malware {
    meta:
        author = "l"
        description = "Detectar por strings"
        date = "15/09"

    strings:
        $a = "vssadmin"
        $b = "delete"
        $c = "shadows"
        $d = "all"
        $e = "quiet"

    condition:
        all of them
}

rule malwaa {
    meta:
        author = "l"
        description = "Detectar por strings"
        date = "15/09"

    strings:
        $a = "bcdedit"
        $b = "set"
        $c = "default"
        $d = "recoveryenabled"
        $e = "no"

    condition:
        all of them
}

rule mal {
    meta:
        author = "l"
        description = "Detectar por strings"
        date = "15/09"

    strings:
        $a = "bcdedit"
        $b = "set"
        $c = "default"
        $d = "bootstatuspolicy"
        $e = "default"

    condition:
        all of them
}
