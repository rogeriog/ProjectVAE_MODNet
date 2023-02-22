import os
import glob

ga_instance_path = './tmp/ga_instance_generation_*.pkl'
latest_file = max(glob.iglob(ga_instance_path), key=os.path.getctime, default=None)

if latest_file is not None:
    print(f'Last modified GA instance file: {latest_file}')
else:
    print('No GA instance file found in ./tmp folder')