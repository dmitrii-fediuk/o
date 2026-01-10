https://en.wikipedia.org/wiki/Reason_maintenance

#
**Reason maintenance** is a **knowledge representation approach** to **efficient handling** of **inferred information** that is **explicitly stored**. 

#
Reason maintenance **distinguishes** between **base facts**, which **can be defeated**, and **derived facts**.

#
As such it **differs from belief revision** which, in its basic form, **assumes** that **all facts are equally important**

#
Reason maintenance was **originally developed** as a **technique** for **implementing problem solvers**.
#
It encompasses a variety of techniques that share a **common architecture**: **2 components**
- a **reasoner** 
- a **reason maintenance system**
##
They **communicate** with each other **via an interface**. 
## Reasoner
###
The reasoner uses the reason maintenance system to **record its inferences** and **justifications** of ("reasons" for) the inferences. 
###
The reasoner also **informs** the reason maintenance system which are **the currently valid base facts (assumptions)**. 
## Reason Maintenance System
The reason maintenance system **uses the information** to **compute the truth value** of the **stored derived facts** and to **restore consistency** **if an inconsistency is derived**.

# Truth maintenance system
https://en.wikipedia.org/wiki/Reason_maintenance#Truth_maintenance_system



