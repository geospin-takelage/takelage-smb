#!/usr/bin/env bash
_smbpasswd_completions()
{
    IFS=$'\n' read -d '' -r -a smbusers < /etc/samba/smbusers
    for userid in "${!smbusers[@]}";
    do
        smbusers[$userid]=$(echo ${smbusers[$userid]} | cut -d '=' -f 1)
    done

    COMPREPLY=($(compgen -W "${smbusers[*]}"))
}

complete -F _smbpasswd_completions smbpasswd