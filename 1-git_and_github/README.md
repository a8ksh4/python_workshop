
[Return to Index](../)

# Git and Github:
## Setup
**Create github account**  
[www.github.com](www.github.com)  
Don't forget about two factor authenticaion if you're going to put real code in there.  Github has free private repositories for students.  Bitbucket has free private repositories for everyone. This course uses Github, though.  
  
**Install Git**:  
* Linux
  * apt-get install git
* Mac
  * XCode
  * Homebrew
  * [Package](https://git-scm.com/)
* Windows
  * [Package with installer](https://git-scm.com/) - Git comes with a convenient bash shell!
  
**(Generate and) Sync ssh keys with Github**  
  
**Clone this repository!**  
  
## Info:
**VCS**  
* [Centralized vs. Decentralized](https://www.youtube.com/watch?v=yPgAfj20PT8)
  
**Git**  
* Distributed
* Fast
* Simple Design
* Strong support for parallel branches
* Able to handle large projects efficiently (like the linux kernel)

**Reference**  
* [The Git Parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html)
* [A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/)
* [Git Workflow](https://www.youtube.com/watch?v=3a2x1iJFJWc)
* [Github Overview](https://www.youtube.com/watch?v=v95nmWwR8rQ)
* [Git Demo](https://www.youtube.com/watch?v=9pa_PV2LUlw)
  
## Assignment
This is stolen outright from the Georgia Tech ["Software Development Process" class](https://www.udacity.com/wiki/ud957)!

If this seems impossible, watch the "Git Demo" above. Use the GitHub "Network" view to monitor the state of your repo during the assignment. 

### Setup
Create a new repository in your github called "exampleprob".  
  
If you mess this up, you can remove and re-create the repository to try again.  
  
### Instructions:
**Part 1 (Terminal 1)**
1. Before you start, make sure to specify your name and email address using command “git config”, if you haven’t already.
1. Open a terminal window
1. Create and go to directory User1
1. Clone REPO
1. This should create a directory called *exampleprob* under directory User1.
1. Go to directory *exampleprob*  (here you can also open the Network view in GT GitHub and start monitoring how your repository evolves)
1. Make sure that the directory contains a file called MyPrivateRepo
1. Create and go to directory Assignment2 (under *exampleprob*)
1. Create a file called myinfo.txt that contains only one line with your first and last name
1. Commit the file to your local repo with comment “Added myinfo file”
1. Create a branch called “development” and switch to it
1. Create a file called dev1.txt that contains the text “Dev 1 file”.
1. Commit the file to your local repo (it should be in branch “development”) with comment “Added dev1 file”
1. Switch to the “master” branch
1. Edit file myinfo.txt and add your zip code in a separate line (feel free to make up the code, if you don't want to use yours)
1. Commit the file to your local repo with comment “Edited myinfo file”
1. Merge the “development” branch into the “master” branch with commit message “Merge #1”
1. Push all branches to the remote repository
  
**Part 2 (Terminal 2)**
1. Open a second terminal window
1. Create and go to directory User2
1. Clone REPO
1. Just like before, this should create a directory called *exampleprob* under directory User2
1. Go to directory *exampleprob*/Assignment2
1. Switch to the “development” branch
1. Create a file called dev2.txt that contains the text “Dev 2 file”.
1. Commit the file to your local repo (it should be in branch “development”) with comment “Added dev2 file”
1. Create a branch called “temp” and switch to it
1. Create a file called mytemp.txt that contains the text “Mytemp file”.
1. Commit the file to your local repo (it should be in branch “temp”) with comment “Added mytemp file”
1. Create and commit to branch “development”, with the usual comment, a file called dev3.txt that contains the text “Dev 3 file”.
1. Merge the “temp” branch into the “development” branch with commit message “Merge #2”
1. Merge the “development” branch into the “master” branch with commit message “Merge #3”
1. In the master branch, edit file myinfo.txt and add your login name (e.g., gpburdell27)
1. Commit the file to your local repo with comment “Edited myinfo file again”
1. Push all branches to the remote repository
  
**Part 3 (Terminal 1)**
1. Go back to the first terminal
1. Make sure to be in branch “master”
1. Edit file myinfo.txt and add your phone number in a separate line (feel free to use a fake phone number)
1. Commit the file to your local repo with comment “Edited myinfo file for the third time”
1. Push the master to the remote repository. To do so, you will have to suitably pull changes from the remote repository and handle conflicts. In handling conflicts, make sure not to lose any content, not to have any of the extra text added by Git to mark the conflicting parts, and to preserve the order of the information as it appears in the assignment (i.e., first and last name, zip code, GT Username, and phone number). Use commit message “Final merge with conflicts fixed” for the additional commit after merging and handling the conflicts.
1. Tag the current version of the master as “V1” and push the tag to the remote repository. Use a lightweight tag. 
  
At this point you are done, and your remote repository should look like the one in the figure below in the "Network" view on your github. If it doesn’t, it means that you made a mistake in one of the steps.  
  
![Graph Reference](./.ignore/graph_reference.png)
