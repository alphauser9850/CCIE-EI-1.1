# Connect to your ESXi server
$Server = "150.1.7.105"
$User = "root"
$Password = "Droidzzz@123"
Connect-VIServer -Server $Server -User $User -Password $Password

# Specify the VM and the snapshot name you want to revert to
$VMName = "DNAC"
$SnapshotName = "Initial_config"

# Get the VM object
$VM = Get-VM -Name $VMName

# Get the snapshot object
$Snapshot = Get-Snapshot -VM $VM -Name $SnapshotName

# Revert to the snapshot
Set-VM -VM $VM -Snapshot $Snapshot -Confirm:$false

# Disconnect from the ESXi server
Disconnect-VIServer -Server $Server -Confirm:$false
