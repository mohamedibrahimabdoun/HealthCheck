
$computers= (Get-Content -path C:\HealthCheck\servers.txt)
#$Logs =$("System", "Application")
#$computer=$computers
foreach($computer in $computers)
{


$computer.ToString()


$events = Get-EventLog -ComputerName $computer -LogName Application  -After ((Get-Date).adddays(-7)) -EntryType Error,Warning | select-Object TimeGenerated,Index,EventID,MachineName,Category,EntryType,Message

#$connectionString = "Data Source=172.26.180.126\;Integrated Security=true;Initial Catalog=test_db;"
$connectionString ="Data Source=172.26.180.126;Initial Catalog=test_db;User ID=healthcheck;Password=Zain@1234;"
$bulkCopy = new-object ("Data.SqlClient.SqlBulkCopy") $connectionString
$bulkCopy.DestinationTableName = "dbspace"
$dt = New-Object "System.Data.DataTable"

# build the datatable
$cols = $events | select -first 1 | get-member -MemberType NoteProperty | select -Expand Name
foreach ($col in $cols)  {$null = $dt.Columns.Add($col)}
  
foreach ($event in $events)
  {
     $row = $dt.NewRow()
     foreach ($col in $cols) { $row.Item($col) = $event.$col }
     $dt.Rows.Add($row)
  }
  
 # Write to the database!
 $bulkCopy.WriteToServer($dt)
 $dt.Rows.Count
}
