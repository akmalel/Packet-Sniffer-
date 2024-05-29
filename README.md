
Prerequisites: 
  nCAP-1.79
  Python 3.7+ (Tested on 3.12)
  
  To run the script, open your Command Prompt with administrative privileges and use the following command format, replacing the interface_name with the actual name of your network interface:

        "py PythonApplication1.py -i "interface_name" -c 10 -f "tcp port 80" -o captured_packets.p"

For Example:    
        "py PythonApplication1.py -i "Wi-Fi" -c 10 -f "tcp port 80" -o captured_packets.pcap" and or "py PythonApplication1.py -i "Ethernet" -c 10 -f "tcp port 80" -o captured_packets.pcap"


