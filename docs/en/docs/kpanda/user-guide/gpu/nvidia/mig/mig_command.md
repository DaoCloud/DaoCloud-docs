# MIG Related Commands

GI Related Commands:

| Subcommand                              | Description                   |
| --------------------------------------- | ----------------------------- |
| nvidia-smi mig -lgi                   | View the list of created GI instances          |
| nvidia-smi mig -dgi -gi {Instance ID} | Delete a specific GI instance            |
| nvidia-smi mig -lgip                  | View the profile of GI           |
| nvidia-smi mig -cgi {profile id}      | Create a GI using the specified profile ID |

CI Related Commands:

| Subcommand                                                  | Description                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| nvidia-smi mig -lcip  { -gi {gi Instance ID}}         | View the profile of CI, specifying `-gi` will show the CIs that can be created for a particular GI instance |
| nvidia-smi mig -lci                                   | View the list of created CI instances                                       |
| nvidia-smi mig -cci {profile id} -gi {gi instance id} | Create a CI instance with the specified GI                                       |
| nvidia-smi mig -dci -ci {ci instance id}              | Delete a specific CI instance                                             |

GI+CI Related Commands:

| Subcommand                                                       | Description                 |
| ------------------------------------------------------------ | -------------------- |
| nvidia-smi mig -i 0 -cgi {gi profile id} -C {ci profile id} | Create a GI + CI instance directly |
