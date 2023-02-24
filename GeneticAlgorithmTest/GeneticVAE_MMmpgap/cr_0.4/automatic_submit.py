import subprocess
import time
import shutil

### because of this memory error bug in tensorflow, I have to submit 
### the job to the cluster and send it again if it crashes
### https://github.com/tensorflow/tensorflow/issues/48545
command = 'sbatch submit.sh'  # Replace with your command

while True:
    # Submit the job
    print('Submitting job...')
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    job_id = stdout.decode().split(' ')[-1].strip()

    # Wait for the job to finish or crash
    while True:
        proc = subprocess.run(f'squeue -j {job_id}', shell=True, stdout=subprocess.PIPE)
        output = proc.stdout.decode()
        if job_id not in output:
            break
        time.sleep(60)

    # Copy the log file
    shutil.copy('log.txt', f'log_{job_id}.txt')

    # Check the return code of the job
    proc = subprocess.run(f'sacct -j {job_id} --format=State --noheader', shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.decode().strip()
    if output == 'COMPLETED':
        print('Job finished successfully.')
        break
    else:
        print(f'Job crashed with status {output}.')
        print('Resubmitting job...')
