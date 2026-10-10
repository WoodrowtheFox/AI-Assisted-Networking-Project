1. Make sure that you have Ookla Speedtest CLI installed and run it once to accept the license.

2. Once you have that installed go to metrics.py and change line 29 to be your file path to speedtest.exe.

3. Make sure that you have done "pip install matplotlib requests" for the final report.

4. Once that is done you can run it by typing in python -m report (Assuming you are using Windows and have python 3.12 or newer installed).

5. It will then prompt you to put in your ISPs advertised download and upload speed in Mbps.

6. After that, you will then enter how many tries for each IP you would like to do.

7. You will then be asked to enter in the IPs that you would like to test(Make sure that they are real/valid IPs that reply to pings). 

8. Once you have entered all the IPs you want to test type EXIT and wait. 

9. Once it is finished, you will find the results in the following files: report.txt, Throughput.png, Packet.png, Latency.png, Jitter.png, and Hops.png.
(The program will output: Report is done! to the terminal when it is finished.)