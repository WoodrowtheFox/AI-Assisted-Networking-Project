1. Make sure that you have speedtest-cli for Desktop installed and run it once to accept the license.

2. Make sure that you have done "pip install matplotlib requests" for the final report.

2. Once you have that installed go to metrics.py and change line 29 to be your file path.

3. Once that is done you can run it by typing in python -m report (Assuming you are using Windows and have python 3.12 or newer installed).

4. It will then prompt you to put in your ISPs advertised download and upload speed in Mbps.

4. After that, you will then enter how many tries for each IP you would like to do.

5. You will then be asked to enter in the IPs that you would like to test. 

6. Once you have entered all the IPs you want to test type EXIT and wait. 

7. Once it is finished, you will find the results in the following files: report.txt, Throughput.png, Packet.png, Latency.png, Jitter.png, and Hops.png.
(The program will output: Report is done! to the terminal when it is finished.)