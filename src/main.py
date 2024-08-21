import subprocess, tomllib
from error_handling import base_logger
from pathlib import Path

conf_logger = base_logger("parsingConfiguration")

if __name__ == "__main__":
    
    # parse configuration
    try:
        with open("data.toml", "rb") as f:
            config = tomllib.load(f)
            
    except tomllib.TOMLDecodeError:
        conf_logger.error('An Error occurred when decoding the Config file in the project dir')
        exit(1)
        
    if config['SYSTEM']['riot_dir'] and Path(config['SYSTEM']['riot_dir']).absolute().exists():
        conf_logger.info('Found RIOT directory in config file')
        
        riot_client_dir = Path(config['SYSTEM']['riot_dir']).absolute()
        cmd = [riot_client_dir]
    else:
        conf_logger.error('RIOT directory not found in config file or it does not exist')
        exit(1)

    subprocess.run(cmd, shell=True)

