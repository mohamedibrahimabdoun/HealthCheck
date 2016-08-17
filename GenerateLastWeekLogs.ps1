$SmtpServer = "172.20.4.185"
$Emailfrom = "healthcheck@bh.zain.com"
$EmailTo = "mohamed.osman@bh.zain.com"

Get-EventLog -LogName "Application"  -After ((Get-Date).adddays(-7)) -EntryType Error,Warning | select-Object TimeGenerated,Index,EventID,MachineName,Category,EntryType,Message | export-csv C:\HealthCheck\logs.csv

$message = New-Object System.Net.Mail.MailMessage($Emailfrom, $EmailTo, "HealthCheck", "BTAPP02 Event Logs for the last week has been generated ")
$message.IsBodyHTML = $true
#$attach = new-object Net.Mail.Attachment($log)
#$message.Attachments.Add($attach)
$smtp = new-object Net.Mail.SmtpClient($SmtpServer)
        
# Sending email
$smtp.Send($message)
#$attach.Dispose()
$message.Dispose()