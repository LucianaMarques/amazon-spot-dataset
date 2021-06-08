# Amazon Spot instances price dataset

This repository contains scripts to automatically capture data from AWS's spot instances via command line.

## Instructions

1. Install [AWS CLI](https://aws.amazon.com/cli/)
2. In scripts folder, open `save_data.sh`, edit the path you want to save data and then run `$ chmod +x save_data.sh && ./save_data.sh`
3. For plotting data, run `plot_images.py`. You need to have Python 3 installed and this will by default plot only Linux instances, for other instances you need to change it in the script;
4. For retrieving technical specifications for each instance, run `save_instance_types.sh`.

## Current Data


