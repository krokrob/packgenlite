Data analysis
==============
- Document here the project: {proj}
- Description: {description}
- Data Source:
- Type of analysis:

Please document the project the better you can.

Stratup the project
=====================
The initial setup.

Create virtualenv and install the project::

  $ sudo apt-get install virtualenv python-pip python-dev
  $ deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt

Unittest test::

  $ make clean install test


Check for {proj} in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/{proj}`
- Then populate it:

  $ ##   e.g. if group is "{group}" and project_name is "{proj}"
  $ git remote add origin git@gitlab.com:{group}/{proj}.git
  $ git push -u origin master
  $ git push -u origin --tags

Functionnal test with a script::

  $ cd /tmp
  $ {proj}-run

Install
==========
Go to `gitlab.com/{group}/{proj}` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it::

  $ sudo apt-get install virtualenv python-pip python-dev
  $ deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate

Clone the project and install it::

  $ git clone gitlab.com/{group}/{proj}
  $ cd {proj}
  $ pip install -r requirements.txt
  $ make clean install test                # install and test

Functionnal test with a script::

  $ cd /tmp
  $ {proj}-run

Continus integration
=====================
Every push of `master` branch will execute `.gitlab-ci.yml` docker jobs.

Prod deployement
================


Install
---------
Install ansible

Check version::

 $ ansible 2.xx.x.x
 config file = /etc/ansible/ansible.cfg
 configured module search path = Default w/o overrides
 python version = 2.7.13 (default, Jan 19 2017, 14:48:08) [GCC 6.3.00170118]

Be sure you SSH public key is know by the host.
Set the server in ansible/all.serverlist::

 e.g
 [kvm05]
 87.98.197.5   ansible_user=root     ansible_ssh_user=root


Deploy prod
------------
::

 $ make prod_install
