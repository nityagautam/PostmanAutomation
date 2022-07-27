@echo on
title "Automation Demo for Postman"
color a
cls
prompt "Execution:: [$t$d] "
echo Changing the path now ...
cd C:\Users\nfaruqe\Desktop\New_Postman_collections\BankingServices" 
echo ""
cls
newman run "Sample API Test01.postman_collection.json" -e "Banking Services.postman_environment.variables.json" -r htmlextra,cli --reporter-htmlextra-export "reports/DemoRegressionSuiteReport.html"
cls		
echo "Execution completed ... Press any key to exit"
pause