# System Resource Monitor & Analyzer

## Overview

This project is a simple Python-based system monitoring tool that collects and analyzes system resource usage.

It records the following metrics into a CSV file:

* CPU Usage (%)
* RAM Usage (%)
* Disk Usage (%)

A second script reads the collected data and uses **NumPy** to analyze system performance.

---

## Features

* Monitor CPU, RAM, and Disk usage
* Store data in a CSV file
* Read and process CSV data
* Calculate:

  * Average usage
  * Maximum usage
  * Minimum usage
  * Standard Deviation
* Practice working with NumPy arrays and statistical analysis

---

## Technologies Used

* Python 3
* psutil
* csv
* NumPy

---

## Project Structure

```text
.
├── system_logger.py      # Collects system metrics
├── system_analyzer.py    # Reads CSV and analyzes data
├── system_log.csv
└── README.md
```

---

## Installation

Install the required packages:

```bash
pip install psutil numpy
```

---

## Usage

### Step 1: Collect system data

Run:

```bash
python system_logger.py
```

This creates or updates:

```text
system_log.csv
```

---

### Step 2: Analyze the collected data

Run:

```bash
python system_analyzer.py
```

Example output:

```text
Average
CPU: 15.2
RAM: 12.1
DISK: 68.0

Maximum
CPU: 16.0
RAM: 12.2
DISK: 68.0

Minimum
CPU: 14.8
RAM: 12.0
DISK: 68.0

Standard Deviation
CPU: 0.43
RAM: 0.06
DISK: 0.00
```

---

## What I Learned

* Reading and writing CSV files
* Working with Python lists
* Converting strings into numeric values
* Using NumPy arrays
* Calculating statistical metrics:

  * Mean
  * Maximum
  * Minimum
  * Standard Deviation
* Understanding how system performance data can be analyzed

---

## Future Improvements

* Add Matplotlib graphs
* Detect CPU spikes automatically
* Generate performance reports
* Export summaries to JSON
* Monitor network usage
* Add real-time monitoring dashboard

---

## License

This project is for learning purposes.
