# InfoSec Operations
Programming for a safer world to live in!
These are projects related to security scripting in the Python language.


Introduction: (Problem description)

There are a large number of reasons why it’s a good idea to keep apprised of when, where, why, and how a computer is used on a frequent basis. There could be critical indicators of compromise “IOCs” and/or indicators of attacks “IOAs” that could possibly help network defenders protect against such activities or remediate them after the fact. The proper logging of all user and computer activities is crucial to any network defense program and should be carefully implemented in addition to password policy enforcement. Computer logs lie deep inside of a computer’s hard drive residing on each individual computer and server alike and getting access to those data repositories can be a daunting task. Having to log into 5, 10, 20 or more computers multiple times throughout the day is not manageable nor feasible let alone cost efficient.

Five common reasons to monitor computer logs:
 1 Superior data breach detection:
      Real-Time alerts through activity monitoring and PC resource utilization thresholds
 2 Reduced time-to-repair TTR:
      Dates, times, and previous state information helps establish timelines, which in the end helps push post incident investigations                towards a speedier recovery.
 3 Low-cost regulatory compliance:
      Faster audits through reduced data and interface management.
 4  Efficient vendor activity auditing:
      Better enforcement of third-party SLAs through activity enforcement and transparency.
 5  More efficient forensic investigations:
      Being able to quickly and efficiently correlate log data provides a more comprehensive IT cybersecurity management solution.

So the solution is to automate these tasks that will in turn reduce time and costs to managing networks of any size. Enter Python scripting, a way to preprogram automated scripting that can simultaneously log into multiple machines and transfer log file data “securely’ to a centralized machine, designated by the network administrator, to be parsed at a later time for potential IOCs and/or IOAs.

Major features and solution

Required Python Modules
Python modules are prefabricated definitions and statements that provide additional functionality after importing them into Python scripts. The following modules and their associated functionality are outlined below:
SSH (Parameko): 
A remote login program that establishes a secured connection prior to sending username and password data onto an untrusted network or a trusted network as an added layer of security.

