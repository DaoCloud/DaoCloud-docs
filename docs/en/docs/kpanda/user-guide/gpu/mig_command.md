# MIG Commands

GI related commands:

| Subcommand                            | Description                     |
| ------------------------------------- | ------------------------------- |
| nvidia-smi mig -lgi                   | View the list of created GIs     |
| nvidia-smi mig -dgi -gi {Instance ID} | Delete the specified GI instance |
| nvidia-smi mig -lgip                  | View the `profile` of GIs        |
| nvidia-smi mig -cgi {profile id}      | Create a GI with the specified profile ID |

CI related commands:

| Subcommand                                                  | Description                                                                                    |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| nvidia-smi mig -lcip  { -gi {gi Instance ID}}              | View the `profile` of CIs, specifying `-gi` shows the CIs that can be created for a specific GI |
| nvidia-smi mig -lci                                         | View the list of created CI instances                                                         |
| nvidia-smi mig -cci {profile id} -gi {gi instance id}       | Create a CI with the specified GI and CI profile IDs                                           |
| nvidia-smi mig -dci -ci {ci instance id}                    | Delete the specified CI instance                                                               |

GI+CI related command:

| Subcommand                                                       | Description             |
| ---------------------------------------------------------------- | ----------------------- |
| nvidia-smi mig -i 0 -cgi {gi profile id} -C {ci profile id}    | Create a GI + CI instance |
