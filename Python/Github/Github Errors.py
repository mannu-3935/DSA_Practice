'''
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> git push                                                   
remote: Permission to mannu-3935/DSA_Practice.git denied to anshu-cloud.
fatal: unable to access 'https://github.com/mannu-3935/DSA_Practice.git/': The requested URL returned error: 403

git config user.name "mannu-3935"  
git config user.email "mannudongre3935@gmail.com"  

git remote set-url origin git@github.com:mannu-3935/DSA_Practice.git
git push

'''






'''
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> ls ~/.ssh


    Directory: C:\Users\manisha\.ssh


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        23-03-2026     15:14             92 known_hosts


PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> ssh-keygen -t ed25519 -C "mannudongre3935@gmail.com" -f ~/.ssh/id_ed25519 -N ""
option requires an argument -- N
usage: ssh-keygen [-q] [-a rounds] [-b bits] [-C comment] [-f output_keyfile]
                  [-m format] [-N new_passphrase] [-O option]
                  [-t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa]
                  [-w provider] [-Z cipher]
       ssh-keygen -p [-a rounds] [-f keyfile] [-m format] [-N new_passphrase]
                   [-P old_passphrase] [-Z cipher]
       ssh-keygen -i [-f input_keyfile] [-m key_format]
       ssh-keygen -e [-f input_keyfile] [-m key_format]
       ssh-keygen -y [-f input_keyfile]
       ssh-keygen -c [-a rounds] [-C comment] [-f keyfile] [-P passphrase]
       ssh-keygen -l [-v] [-E fingerprint_hash] [-f input_keyfile]
       ssh-keygen -B [-f input_keyfile]
       ssh-keygen -D pkcs11
       ssh-keygen -F hostname [-lv] [-f known_hosts_file]
       ssh-keygen -H [-f known_hosts_file]
       ssh-keygen -K [-a rounds] [-w provider]
       ssh-keygen -R hostname [-f known_hosts_file]
       ssh-keygen -r hostname [-g] [-f input_keyfile]
       ssh-keygen -M generate [-O option] output_file
       ssh-keygen -M screen [-f input_file] [-O option] output_file
       ssh-keygen -I certificate_identity -s ca_key [-hU] [-D pkcs11_provider]
                  [-n principals] [-O option] [-V validity_interval]
                  [-z serial_number] file ...
       ssh-keygen -L [-f input_keyfile]
       ssh-keygen -A [-a rounds] [-f prefix_path]
       ssh-keygen -k -f krl_file [-u] [-s ca_public] [-z version_number]
                  file ...
       ssh-keygen -Q [-l] -f krl_file [file ...]
       ssh-keygen -Y find-principals -s signature_file -f allowed_signers_file
       ssh-keygen -Y match-principals -I signer_identity -f allowed_signers_file
       ssh-keygen -Y check-novalidate -n namespace -s signature_file
       ssh-keygen -Y sign -f key_file -n namespace file [-O option] ...
       ssh-keygen -Y verify -f allowed_signers_file -I signer_identity
                  -n namespace -s signature_file [-r krl_file] [-O option]
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> ssh-keygen -t ed25519 -C "mannudongre3935@gmail.com" -f ~/.ssh/id_ed25519
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again: 
Saving key "~/.ssh/id_ed25519" failed: No such file or directory
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> ssh-keygen -t ed25519 -C "mannudongre3935@gmail.com" -f "C:\Users\manisha\.ssh\id_ed25519"
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in C:\Users\manisha\.ssh\id_ed25519
Your public key has been saved in C:\Users\manisha\.ssh\id_ed25519.pub
The key fingerprint is:
SHA256:yG7g4oWb1izkCltOimQ7HgRKc55nKCZGRVsZbFHmWFQ mannudongre3935@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|  .o.+*=.E       |
|  . o+=          |
|.+ o.. .         |
|= + o. .         |
|o= +.oo S        |
|= oooo           |
|.*=oo o          |
|=O*=o.           |
|*=*.             |
+----[SHA256]-----+
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> Start-Service ssh-agent; ssh-add "C:\Users\manisha\.ssh\id_ed25519"
Start-Service : Service 'OpenSSH Authentication Agent (ssh-agent)' cannot be started due to the 
following error: Cannot start service ssh-agent on computer '.'.
At line:1 char:1
+ Start-Service ssh-agent; ssh-add "C:\Users\manisha\.ssh\id_ed25519"
+ ~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OpenError: (System.ServiceProcess.ServiceController:ServiceController) [  
   Start-Service], ServiceCommandException
    + FullyQualifiedErrorId : CouldNotStartService,Microsoft.PowerShell.Commands.StartServiceCommand    

Error connecting to agent: No such file or directory
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> Get-Content "C:\Users\manisha\.ssh\id_ed25519.pub"
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPoEZw2AmQpAfek/aUPQA+UqVCxJpzlrnj9cS/tT6cZG mannudongre3935@gmail.com
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> git push
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> Set-Service -Name ssh-agent -StartupType Automatic; Start-Service ssh-agent
Set-Service : Service 'OpenSSH Authentication Agent (ssh-agent)' cannot be configured due to the 
following error: Access is denied
At line:1 char:1
+ Set-Service -Name ssh-agent -StartupType Automatic; Start-Service ssh ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (System.ServiceProcess.ServiceController:ServiceContro  
   ller) [Set-Service], ServiceCommandException
    + FullyQualifiedErrorId : CouldNotSetService,Microsoft.PowerShell.Commands.SetServiceCommand        

+ ... rvice -Name ssh-agent -StartupType Automatic; Start-Service ssh-agent
+                                                   ~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OpenError: (System.ServiceProcess.ServiceController:ServiceController) [
   Start-Service], ServiceCommandException
    + FullyQualifiedErrorId : CouldNotStartService,Microsoft.PowerShell.Commands.StartServiceCommand

PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> ssh -T git@github.com
Enter passphrase for key 'C:\Users\manisha/.ssh/id_ed25519':
Hi mannu-3935! You've successfully authenticated, but GitHub does not provide shell access.
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice> git push
Enter passphrase for key '/c/Users/manisha/.ssh/id_ed25519':
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 8 threads
Compressing objects: 100% (11/11), done.
Writing objects: 100% (13/13), 1.50 KiB | 54.00 KiB/s, done.
Total 13 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:mannu-3935/DSA_Practice.git
   f426800..1cb9c73  main -> main
PS C:\Users\manisha\OneDrive\Desktop\DSA Practice\DSA_Practice>
'''