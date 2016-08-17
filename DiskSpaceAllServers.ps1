
$computers= (Get-Content -path C:\HealthCheck\servers.txt)
foreach($computer in $computers)
{

  $txt="=============$computer  ============================" 

 $obj=Get-WmiObject  -ComputerName $computer  -Class Win32_Volume -Filter "DriveType = 3" | Format-Table  -auto @{Label="Drive";` 
            Expression={$_.DriveLetter};` 
            Align="Right"},` 
         @{Label="Free(GB)";` 
            Expression={"{0:N0}" -f ($_.FreeSpace/1GB)};` 
            Align="Right"},` 
         @{Label="% Free";` 
            Expression={"{0:P0}" -f ($_.FreeSpace / $_.Capacity)};` 
            Align="Right"},` 
         @{Label="Size(GB)";` 
            Expression={"{0:N0}" -f ($_.Capacity / 1GB)};` 
            Align="Right"},` 
         @{Label="Volume Label";` 
            Expression={$_.Label};` 
            Width=25}
  $endtxt="=========================================================================================================="          
           $txt| out-file -append -filepath "C:\HealthCheck\Drive Space.txt"
           $obj| out-file -append -filepath "C:\HealthCheck\Drive Space.txt"
           $endtxt| out-file -append -filepath "C:\HealthCheck\Drive Space.txt"

}