#SRI Invoice Downloader & Reporter
projects = [
     {
        "name": "Sistema de facturación",
        "description": None,
        "img_url": [],
        "technologies": ["Python"],
     },
     {
        "name": "Tesis analisis de datos",
        "description": None,
        "img_url": [],
        "technologies": ["Python"],
     },
    {
        "name": "Analisis poblacion Cotopaxi",
        "description": None,
        "img_url": [],
        "technologies": ["Python"],
     },
    {
        "name": "SRI Invoice Automation System",
        "description": '''
        Developed a software solution to automate the retrieval and management of electronic invoices through the SRI web service. The system automatically downloads invoice information, generates the corresponding PDF documents, and organizes them into folders according to the billing month.
        
        The application also processes the collected information to generate a tax reporting file, providing a structured summary of the invoices and amounts required to complete the corresponding tax declaration through the SRI online portal. This significantly reduces manual data entry and simplifies the process of managing and preparing electronic invoices for tax reporting.
        ''',
        "img_url": [f"project2-{i}.png" for i in range(1,4)],
        "technologies": ["Python", "Qt", "Web Services/SOAP", "XML", "PDF generatión", "Data processing", "Automation"],
    },
    {
        "name": "A Low Cost Robotic Medical Simulator for CPR Training",
        "description": '''
        Developed the <strong>software architecture</strong> and <strong>real-time monitoring system</strong> for a robotic medical simulator designed for <strong>cardiopulmonary resuscitation training</strong>. The system was implemented using <strong>Python</strong> connecting via <strong>TCP/IP</strong> with a <strong>Raspberry Pi</strong>, integrating multiple <strong>sensors and actuators</strong> to monitor and control the simulator in real time.
        <br><br>
    
        The software <strong>acquires and processes sensor data in real time</strong> to evaluate CPR performance, controls actuators to simulate physiological responses, and enables real-time visualization and <strong>generation of ECG waveforms and cardiac rhythms</strong>. It also allows configure and execute clinical scenarios with immediate feedback .<br><br>
    
        The project resulted in a <strong>peer-reviewed scientific publication</strong>: <em>A Low Cost Robotic Medical Simulator for CPR Training</em>, published in <a href="https://doi.org/10.1088/1757-899X/575/1/012019" style="color: #0fc3ff; text-decoration: underline;">IOP Conference Series: Materials Science and Engineering (2019)</a>.
        ''',
        "img_url": [f"project1-{i}.png" for i in range(1,9)],
        "technologies": ["Python", "Qt", "Numpy", "Raspberry Pi", "PyQtGraph", "Real-Time Data Acquisition", "Sensors & Actuators", "TCP/IP"],
    },
]
