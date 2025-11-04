from iac_patterns.factory import NullResourceFactory
from datetime import datetime
import json
import os

class TimestampedNullResourceFactory(NullResourceFactory):
    @staticmethod
    def create(name: str, fmt: str) -> dict:
        ts = datetime.utcnow().strftime(fmt)
        return NullResourceFactory.create(name,{"time_stamp": ts})


if __name__ == "__main__":
    output_dir = os.path.join("output","timestamped")
    os.makedirs(output_dir,exist_ok=True)
    with open(os.path.join(output_dir,"main.tf.json"),"w") as f:
        json.dump( TimestampedNullResourceFactory.create("test_ts","%Y%m%d"),f,indent=4)
