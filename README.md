<!-- [![N|Solid](https://www.delphix.com/themes/custom/delphix/logo_black.svg)](https://delphix.com) -->

## Purpose
vsdk plugin tester is a tool developed by Delphix professional services team to test any vsdk-plugin like MongoDB, MySQL, Couchbase etc. [ Extensions to Delphix Dynamic Data Platform].  This tool helps to test basic inbuilt functionalities provided by Delphix Dynamic Data Platform to any vsdk plugin. 
Tool is developed using Ansible and has dependencies on 
  - shell script execution
  - [dxtoolkit](https://github.com/delphix/dxtoolkit)

## Test cases covered

##### dSource
  - Create sourceconfig [ source data configuration]  [ Optional ]
  - Create dSource  [ Optional ]
  - Create dSource Snapshot [ Snapsync process ]
  - Disable / Enable dSource

##### VDB
  - Provision VDB  [ Optional]
  - Stop / Start / Disable / Enable VDB
  - Snapshot VDB
  - Create / Delete non-Self-Service Bookmark
  - Refresh / Rewind VDB
  - Rewind VDB to Bookmark / Snapshot Time
  - Refresh VDB using Snapshot Name

##### Self-Service
  - Create / Delete Self-Service Template
  - Create / Delete Self-Service Container
  - Create / Delete Self-Service bookmark
  - Restore to Self-Service bookmark / point-in-time / Template Timeline
  - Refresh Container
  - Create Branch
  - Activate Latest Branch
  - Add Self-Service bookmarks using snapshots in template

> This pretty much covers all the regularly used operations 
> provided by Delphix Dynamic Data Platform to vsdk plugin.

## Pre-Requisites

  - Configured Delphix Engine
  - Staging environments added to delphix engine
  - Target environments added to delphix engine
  - dSource Created [ Optional ]
  - VDB Created [Optional]
  - Ansible installed on testing host [ laptop or central location – UNIX/ Windows (Ubuntu) ]

## Installation
  - Install Ansible [If not already installed]. Ansible Version 2.7.x and above.
  - Download vsdk plugin tester
  - Install dxtoolkit  [ if not already installed ]
  - Update followings configuration files in framework
    - vsdk-plugin-tester/setup/vars/tests_vars.yml  [ see next sections ]
    - vsdk-plugin-tester/setup/vars/<vsdk-plugin>.yml for e.g.
        - vsdk-plugin-tester/setup/vars/mongo.yml
        - vsdk-plugin-tester/setup/vars/couchbase.yml
        - vsdk-plugin-tester/setup/vars/mysql.yml

## Configure vsdk plugin tester

Update the configuration file as per your environment. See below for reference

#### vsdk-plugin-tester/setup/vars/tests_vars.yml

| Variable | Description |
| ------ | ------ |
| DXLOC  | Put full path to dxtoolkit folder |
| DELPHIX_ENGINE_IP | FQDN / IP of delphix engine |
| DELPHIX_ADMIN_USER | Delphix Admin User |
| DELPHIX_ADMIN_PASSWORD | Delphix Admin Password |
| EDSI_TEMPLATE_NAME | This is name of your vsdk-plugin. It can be any name. Same name file with extension .yml must exist in same folder  |
| dSource Parameters Section | Update all parameters as per your environment.These parameters will be referred in ansible jinja2 templates |
| VDB Parameters Section | Update all parameters as per your environment.These parameters will be referred in ansible jinja2 templates |
| CREATE_VDB | True or False [ Advanced ] |
| CREATE_DSOURCE | True or False [ Advanced ] |

#### vsdk-plugin-tester/setup/vars/[mongo.yml] / [couchbase.yml] / [mysql.yml] / [\<vsdk-plugin>.yml]
This is vsdk plugin specific file and defines the parameters that are not covered in test_vars.yml. For any new data source if file does not exists, create new file. File name without extension should match with parameter "EDSI_TEMPLATE_NAME" mentioned in vsdk-plugin-tester/setup/vars/tests_vars.yml
- Add / Update / Delete parameters as per requirement in this file

#### Advanced Configuration

If you want plugin tester to create dSource and VDB, you will need to configure/provide following files:

| File Name | Description |
| ------ | ------ |
| vsdk-plugin-tester/setup/templates/\<vsdk-plugin>_dsource_sourceconfig.j2  | dSource Source Config parameters |
| vsdk-plugin-tester/setup/templates/\<vsdk-plugin>_dsource_parameters.j2  | dSource Creation parameters |
| vsdk-plugin-tester/setup/templates/\<vsdk-plugin>_vdb_source_parameters.j2  | VDB Creation parameters |
| vsdk-plugin-tester/setup/templates/\<vsdk-plugin>\_vdb_sourceconfig_parameters.j2  | VDB Source Config parameters |

###### Sample Files

| File Name | Description |
| ------ | ------ |
| vsdk-plugin-tester/setup/templates/mongo_dsource_sourceconfig.j2  | dSource Source Config parameters |
| vsdk-plugin-tester/setup/templates/mongo_dsource_parameters.j2  | dSource Creation parameters |
| vsdk-plugin-tester/setup/templates/mongo_vdb_source_parameters.j2  | VDB Creation parameters |
| vsdk-plugin-tester/setup/templates/mongo_vdb_sourceconfig_parameters.j2  | VDB Source Config parameters |


## Test vsdk plugin

Go to vsdk-plugin-tester folder and run ansible playbook as below

```sh
$ cd vsdk-plugin-tester
$ ansible-playbook tests.yml
```

## Notes
- If any test fails, testing framework will exit without continuining further.
- You can add following line under [defaults] section in ansible.cfg to get timings for all the ansible tasks.

```sh
callback_whitelist = profile_tasks
```

- Always try to use smallest possible size dSource and VDB. Purpose of the framework is to test the functionality rather than actual ingestion and operations of production dSource / VDB. Though it will work but the number of tests done by this framework is enormous and will take days for all tests to complete for big size databases compared to 30-60 mins / few hours for smaller databases.

## License

This is code is licensed under the Apache License 2.0. Full license is available [here](./LICENSE).