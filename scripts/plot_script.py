import pandas as pd
import json
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt

instances = ['a1.2xlarge', 'g2.8xlarge', 'm4.large', 'p3.16xlarge', 'r5.metal',
             'g3.16xlarge', 'm4.xlarge', 'p3.2xlarge', 'r5n.12xlarge',
             'a1.4xlarge', 'g3.4xlarge', 'm5.12xlarge', 'p3.8xlarge', 'r5n.16xlarge',
             'a1.large', 'g3.8xlarge', 'm5.16xlarge', 'p3dn.24xlarge', 'r5n.24xlarge',
             'a1.medium', 'g3s.xlarge', 'm5.24xlarge', 'r3.2xlarge', 'r5n.2xlarge',
             'a1.metal', 'g4dn.12xlarge','m5.2xlarge', 'r3.4xlarge','r5n.4xlarge',
             'a1.xlarge', 'g4dn.16xlarge',  'm5.4xlarge',  'r3.8xlarge', 'r5n.8xlarge',
             'c1.medium', 'g4dn.2xlarge', 'm5.8xlarge', 'r3.large', 'r5n.large',
             'c1.xlarge', 'g4dn.4xlarge', 'm5a.12xlarge', 'r3.xlarge',  'r5n.xlarge',
             'c3.2xlarge', 'g4dn.8xlarge',  'm5a.16xlarge', 'r4.16xlarge', 'r5.xlarge',
             'c3.4xlarge', 'g4dn.xlarge', 'm5a.24xlarge', 'r4.2xlarge', 't1.micro',
             'c3.8xlarge', 'h1.16xlarge', 'm5a.2xlarge', 'r4.4xlarge', 't2.2xlarge',
             'c3.large', 'h1.2xlarge', 'm5a.4xlarge', 'r4.8xlarge', 't2.large',
             'c3.xlarge', 'h1.4xlarge', 'm5a.8xlarge', 'r4.large', 't2.medium',
             'c4.2xlarge', 'h1.8xlarge', 'm5ad.12xlarge', 'r4.xlarge', 't2.micro',
             'c4.4xlarge', 'hi1.4xlarge', 'm5ad.16xlarge', 'r5.12xlarge', 't2.nano',
             'c4.8xlarge', 'hs1.8xlarge', 'm5ad.24xlarge', 'r5.16xlarge', 't2.small',
             'c4.large', 'i2.2xlarge', 'm5ad.2xlarge', 'r5.24xlarge', 't2.xlarge',
             'c4.xlarge', 'i2.4xlarge', 'm5ad.4xlarge', 'r5.2xlarge', 't3.2xlarge',
             'c5.12xlarge', 'i2.8xlarge', 'm5ad.8xlarge', 'r5.4xlarge', 't3a.2xlarge',
             'c5.18xlarge', 'i2.xlarge', 'm5ad.large', 'r5.8xlarge', 't3a.large',
             'c5.24xlarge', 'i3.16xlarge', 'm5ad.xlarge', 'r5a.12xlarge', 't3a.medium',
             'c5.2xlarge', 'i3.2xlarge', 'm5a.large', 'r5a.16xlarge', 't3a.micro',
             'c5.4xlarge', 'i3.4xlarge', 'm5a.xlarge', 'r5a.24xlarge', 't3a.nano',
             'c5.9xlarge', 'i3.8xlarge', 'm5d.12xlarge', 'r5a.2xlarge', 't3a.small',
             'c5d.12xlarge', 'i3en.12xlarge',  'm5d.16xlarge', 'r5a.4xlarge', 't3a.xlarge',
             'c5d.18xlarge', 'i3en.24xlarge',  'm5d.24xlarge', 'r5a.8xlarge', 't3.large',
             'c5d.24xlarge', 'i3en.2xlarge', 'm5d.2xlarge', 'r5ad.12xlarge', 't3.medium',
             'c5d.2xlarge', 'i3en.3xlarge', 'm5d.4xlarge', 'r5ad.16xlarge', 't3.micro',
             'c5d.4xlarge', 'i3en.6xlarge', 'm5d.8xlarge', 'r5ad.24xlarge', 't3.nano',
             'c5d.9xlarge', 'i3en.large', 'm5d.large', 'r5ad.2xlarge', 't3.small',
             'c5d.large', 'i3en.metal', 'm5d.metal', 'r5ad.4xlarge', 't3.xlarge',
             'c5d.metal', 'i3en.xlarge', 'm5dn.12xlarge', 'r5ad.8xlarge', 'u-12tb1.metal',
             'c5d.xlarge', 'i3.large', 'm5dn.16xlarge', 'r5ad.large', 'u-18tb1.metal',
             'c5.large', 'i3.metal', 'm5dn.24xlarge', 'r5ad.xlarge', 'u-24tb1.metal',
             'c5.metal', 'i3.xlarge', 'm5dn.2xlarge', 'r5a.large', 'u-6tb1.metal',
             'c5n.18xlarge', 'inf1.24xlarge', 'm5dn.4xlarge', 'r5a.xlarge', 'u-9tb1.metal',
             'c5n.2xlarge', 'inf1.2xlarge', 'm5dn.8xlarge', 'r5d.12xlarge', 'x1.16xlarge',
             'c5n.4xlarge', 'inf1.6xlarge', 'm5dn.large', 'r5d.16xlarge', 'x1.32xlarge',
             'c5n.9xlarge', 'inf1.xlarge', 'm5dn.xlarge', 'r5d.24xlarge', 'x1e.16xlarge',
             'c5n.large', 'm1.large', 'm5d.xlarge', 'r5d.2xlarge', 'x1e.2xlarge',
             'c5n.xlarge', 'm1.medium', 'm5.large', 'r5d.4xlarge', 'x1e.32xlarge',
             'c5.xlarge', 'm1.small', 'm5.metal', 'r5d.8xlarge', 'x1e.4xlarge',
             'cc1.4xlarge', 'm1.xlarge', 'm5n.12xlarge', 'r5d.large', 'x1e.8xlarge',
             'cc2.8xlarge', 'm2.2xlarge', 'm5n.16xlarge', 'r5d.metal', 'x1e.xlarge',
             'cg1.4xlarge', 'm2.4xlarge', 'm5n.24xlarge', 'r5dn.12xlarge', 'z1d.12xlarge',
             'cr1.8xlarge', 'm2.xlarge', 'm5n.2xlarge', 'r5dn.16xlarge', 'z1d.2xlarge',
             'd2.2xlarge', 'm3.2xlarge', 'm5n.4xlarge', 'r5dn.24xlarge', 'z1d.3xlarge',
             'd2.4xlarge', 'm3.large', 'm5n.8xlarge', 'r5dn.2xlarge', 'z1d.6xlarge',
             'd2.8xlarge', 'm3.medium', 'm5n.large', 'r5dn.4xlarge', 'z1d.large',
             'd2.xlarge', 'm3.xlarge', 'm5n.xlarge', 'r5dn.8xlarge',  'z1d.metal',
             'f1.16xlarge', 'm4.10xlarge', 'm5.xlarge', 'r5dn.large', 'z1d.xlarge',
             'f1.2xlarge', 'm4.16xlarge', 'p2.16xlarge', 'r5dn.xlarge',
             'f1.4xlarge', 'm4.2xlarge', 'p2.8xlarge', 'r5d.xlarge',
             'g2.2xlarge', 'm4.4xlarge', 'p2.xlarge', 'r5.large']

def get_dataframe(instance_type, product='Linux/UNIX'):
    path='/home/luciana/dev/amazon-spot-dataset/dados-aws-15-02-2021/'
    df = json_normalize(pd.read_json(path+instance_type)['SpotPriceHistory'])
    df['SpotPrice'] = df['SpotPrice'].astype(float)
    return df[df['ProductDescription'] == product].drop(columns=['ProductDescription','InstanceType'])

def save_figure(instance, product='Linux/UNIX'):
    path='/home/luciana/dev/amazon-spot-dataset/figures/dados-30-maio-2021/'
    df = get_dataframe(instance)
    df1 = df[df['AvailabilityZone'] == 'us-east-1a']
    df2 = df[df['AvailabilityZone'] == 'us-east-1b']
    df3 = df[df['AvailabilityZone'] == 'us-east-1c']
    df4 = df[df['AvailabilityZone'] == 'us-east-1d']
    fig, axs = plt.subplots(2, 2, figsize=(15,10))
    axs[0, 0].plot(df1['Timestamp'], df1['SpotPrice'])
    axs[0, 0].set_title('us-east-1a')
    axs[0, 0].set_xticklabels([])
    axs[0, 0].set_xticks([])
    axs[0, 1].plot(df2['Timestamp'], df2['SpotPrice'], 'tab:orange')
    axs[0, 1].set_title('us-east-1b')
    axs[0, 1].set_xticklabels([])
    axs[0, 1].set_xticks([])
    axs[1, 0].plot(df3['Timestamp'], df3['SpotPrice'], 'tab:green')
    axs[1, 0].set_title('us-east-1c')
    axs[1, 0].set_xticklabels([])
    axs[1, 0].set_xticks([])
    axs[1, 1].plot(df4['Timestamp'], df4['SpotPrice'], 'tab:red')
    axs[1, 1].set_title('us-east-1d')
    axs[1, 1].set_xticklabels([])
    axs[1, 1].set_xticks([])
    fig.savefig(instance+'.jpg')
    plt.close()

for instance in instances:
    save_figure(instance)
