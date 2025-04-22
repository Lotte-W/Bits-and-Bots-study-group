# GitHub Guide 
This GitHub Guide is based on the expert session of the Bits and Bots study group, the 2025 cohort. 
It will cover the basic concepts, explain what GitHub is, and how to use it. 
This guide will cover:
* GitHub: Wat is it, intro to GitHub terminology and how to get started
* Markdown and how to use it on GitHub
* Creating an issue and explain what a 'good' issue is
* Repository structure
* Making and Merging pull requests
* Other functionalities, like GitHub pages, and how to turn your GitHub repo into a website
* Further resources.


## What is Git?
Git is a version control system that helps you keep track of file changes. It is also possible to track who made the changes. This makes Git perfect for working with others in writing
code for example. Git is used on platforms such as GitHub, Bitbucket and GitLab. Git and GitHub are two different things.
To learn more about Git, follow the [online course on W3Schools](https://www.w3schools.com/git/default.asp). 

## GitHub
### What is GitHub?
[GitHub](https://github.com/) is a platform that allows anyone to create, store, manage, and share content.
Oftentimes this is code. But that is not the only thing present in GitHub. Here are some
other use cases for GitHub:
* Software development
* Educational resources
* Fanfiction
* Reading lists
* Zines
* Datasets
* Community/crowdsourcing projects
* Blog posts
* Finding file samples
* Documentation

So why is GitHub great to use? GitHub allows people to work collaboratively on any project, with tracking and control settings favouring non-linear workflows and multiple contributions at a time. By tracking everything, there is also a lot of data integrity. 
Additionally, you can use GitHub to let the developers know you have an issue/something is not working.

To start, read more about GitHub [here](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git). One thing to bear in mind is that GitHub, while it is an amazing tool, does come with a lot of jargon. 
A great explanation for some of the terminology around GitHub can be found in this guide.

As digital archivists, we often use open-source tools to aid us with e.g. identifying and validating digital objects or harvesting websites. 
Here are some useful examples of GitHub repositories used in the field that you can find:
* https://github.com/openpreserve/jhove
*  https://github.com/digital-preservation/droid
*   https://github.com/webrecorder/browsertrix-crawler
*    https://github.com/noord-hollandsarchief (see the repositories in this account)

There are a lot of people working with digital archives that use GitHub. This is the reason that it is important for everyone to learn how to use it. Additionally, to show you that it is not just a scary programmer platform. 
A full introductory tutorial on GitHub can be found [here](https://docs.github.com/en/get-started/start-your-journey/hello-world).

### Introduction to GitHub Terminology
A great resource for finding GitHub terminology can be found [here](https://docs.github.com/en/get-started/learning-about-github/github-glossary). 
However, for the purposes of this guide, here is a quick table of basic terms that may help: 
|Term | Definition |
|:---|:-----------|
|**Repository**|A repository is the most basic element of GitHub. They're easiest to imagine as a project's folder. A repository contains all of the project files (including documentation), and stores each file's revision history. Repositories can have multiple collaborators and can be either public or private.|
|**Issue**| Issues are suggested improvements, tasks or questions related to the repository. Issues can be created by anyone (for public repositories), and are moderated by repository collaborators. Each issue contains its own discussion thread. You can also categorise an issue with labels and assign it to someone.|
|**Commit**|A commit, or "revision", is an individual change to a file (or set of files). When you make a commit to save your work, Git creates a unique ID (a.k.a. the "SHA" or "hash") that allows you to keep record of the specific changes committed along with who made them and when. Commits usually contain a commit message which is a brief description of what changes were made.|
|**Branch**|A branch is a parallel version of a repository. It is contained within the repository, but does not affect the primary or main branch allowing you to work freely without disrupting the "live" version. When you've made the changes you want to make, you can merge your branch back into the main branch to publish your changes.|
|**Fork**|A fork is a personal copy of another user's repository that lives on your account. Forks allow you to freely make changes to a project without affecting the original upstream repository. You can also open a pull request in the upstream repository and keep your fork synced with the latest changes since both repositories are still connected.|
|**Push**|To push means to send your committed changes to a remote repository on GitHub.com. For instance, if you change something locally, you can push those changes so that others may access them.|
|**Pull**|Pull refers to when you are fetching changes and merging them. For instance, if someone has edited the remote file you're both working on, you'll want to pull in those changes to your local copy so that it's up to date.|
|**Markdown**|Markdown is an incredibly simple semantic file format, not too dissimilar from .doc, .rtf and .txt. Markdown makes it easy for even those without a web-publishing background to write prose (including with links, lists, bullets, etc.) and have it displayed like a website.|

### Getting Started with GitHub
To create your first GitHub account you will first need to register at www.github.comand follow the instructions provided [here](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github). You will need an email address, password and potentially 2-Factor Authentication.

Once you have created your account in the top right corner you will see a number of buttons. Click on the + sign and then the **New Repository** tab.

![screenshot New Repository](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/New_Repository.png)


A screen will then appear with different options to set up your repository, you will need to keep the repository public to turn it into a website. The main parts to fill out are the name of the repository and a brief description of it. You can add a license if you wish to.
![screenshot Create a New Repository](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Create_a_New_Repository.png)

Tick the box to set up the README, this will tell everyone what your website is about when they come to your page. After clicking create repository then you can create your README. A README for a GitHub repository looks a bit like this below:
![screenshot READme](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/READme.png)

For a basic README you can just type some text in the box to tell everyone what the project is about. However, a README uses a type of programming language called markdown. It is possible to use styling options and add pictures to your README using the Markdown language.

## Markdown
Markdown is a lightweight markup language with a plain text formatting syntax. It is a tool used to convert text to HTML for easy content management. You can use it to write README pages about your repositories in GitHub as well as format GitHub pages. It is
simpler and quicker to write than HTML, if you aren't looking to do anything too complicated. To style words in Markdown, you simply need to surround those words with some special characters. You can use those around one or multiple words. Below are some examples:

![screenshot table markdown](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Markdown_examples.png)

In HTML, there are six headings that you can define with the <h> tag. In Markdown, you simply use a hash mark (#). For heading 1 you use one #, for heading 2 two ## et cetera,
until you are at heading 6: ######
You can also create a heading in bold or italics. 

### Using Markdown on GitHub
With Markdown you can create README files in your GitHub repository. These files can be used to tell other people why your project is useful, what others can do with your project, and how they can use it. The README file is often the first item a visitor will see when visiting your repository.

You can define relative links and image paths in your rendered files to help readers navigate to other files in your repository.

GitHub will automatically transform your relative link or image path based on whatever branch you're currently on, so that the link or path always works. The path of the link will be relative to the current file. Links starting with / will be relative to the repository root. You can use all relative link operands, such as ./ and ../. Relative links are easier for users who clone your repository. Absolute links may not work in clones of your repository - we recommend using relative links to refer to other files within your repository.

## Creating an Issue 
To raise an issue simply go to a repository, for example the Bits-and-Bots-study-group, and click on the issues tab.
![screenshot issue tab](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Issue_tab.png)

You’ll then see a list of all the existing issues, check that nothing similar exists that you can’t already comment on or add to. If that is the case then you can click the Submit New Issue button.

![screenshot new issue](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Submit_new_issue.png)

## What makes a good issue?
Issues should be:
* Very clear, give enough information so that other people can understand the issue as well.
* Try and add detail. The more detail, the better.
* If possible, also try to provide the solution as well as the problem.

This [example of a bad issue](https://github.com/digital-preservation/droid/issues/887) gives insight why we consider this to be a ‘bad’ issue. Someone commented on it that more context should be added, because it is unclear what
the issue is exactly about. 

This other [example of a good issue](https://github.com/digital-preservation/droid/issues/1087), shows that the issue isnmore clear now.

## Repository Structure 
In this section, we explain a bit more on the structure of your repository and how to add, rename and delete files and folders.

You can create new files directly on GitHub in any repository you have writing access to. If you don’t have access to it, you can fork the project to your personal account and send a pull request to the original repository after you commit your change. This is not only the case for adding files, but for all the changes you want to make to a repository you don’t have access to.

To add a file on GitHub of a repository you have writing rights to, navigate to the main page of the repository and browse to the folder where you want to create a file. On the top right, you can select an ‘Add file’ dropdown menu, and then click ‘Create new file’.
![screenshot add file](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Add_file.png)

Type the name and extension for the file in the name field. Content for the file can be typed in the contents text box. If you want to review your content first, click the ‘Preview’ tab on the top left, next to the ‘Edit’ tab. If you’re finished, click on ‘Commit changes…’ (green button on the top right).

If you want to place your newly created file in a new folder, you can use the filename field. Type the name for the folder and end with a / and type the name of the file after the slash in the newly appeared filename field. In the screenshot above you see the name of the directory (Bits-and-Bots-study-group) and the name of the folder (Games) before the filename field. Note how every part is divided by forward slashes.
![screenshot add folder and file](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Add_folder_and_file.png)

A new window will appear for the changes (see screenshot below). Type a brief message that describes the change you made to the file. Below the commit message field, you can choose to add your commit to the current branch or to a new branch. If you create a new one, you can start a pull request.

![screenshot Commit changes](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Commit_changes.png)

It is also possible to upload an existing file. To upload a file, navigate to the main page of the repository and browse to the folder where you want to upload the file. On the top right, you can select an ‘Add file’ dropdown menu, and then click ‘Upload files’. You can choose your files or drag and drop them to add them to the repository. After you’ve done so, you can add a commit message as well, to describe what you have done and choose where you want to commit your changes, just like when you would create a new file. 
![screenshot Upload files](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Upload_files.png)

You can rename any file in your repository directly in GitHub. Simply browse to the file you want to rename, and click on the pencil on the right to edit the file. You can change the name of the file in the filename field, and also update the contents of your file if you want. Click on ‘Commit changes…’ and describe what you’ve done and where you want to commit the changes.
![screenshot Rename file](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Rename_file.png)

Lastly, you can delete an individual file or an entire directory in your repository on GitHub. Browse to the file or the directory you want to delete and select the dropdown menu in the top right corner (with the three dots) and choose ‘Delete file’ or ‘Delete directory’.
![screenshot Delete file](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Delete_file.png)

More on working with files can be found [here](https://docs.github.com/en/repositories/working-with-files)

## Pull requests 
A pull request is a proposal to merge a set of changes from one branch into another.

### Making a Pull Request
To make a pull request, you first need to fork your repository. At the top of your
repository, you can see how many times a repository has been forked.
![screenshot Fork](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Fork.png)

After clicking on this, you get the following:
![screenshot Create fork](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Create_Fork.png)

Now that you have forked the repository, you can make changes such as adding to the README, adding files, etc. While doing this, you can see how many changes you have made by seeing how many commits you are ahead of the original repository. In this example, one sentence has been added to the README.

![screenshot Commit](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Commit_ahead.png)

By selecting contribute, it gives you the option to open a pull request. When selecting this, you can add a title to your pull request along with a description. You can also see what you have changed and how that compares to the original repository.

![screenshot compare changes](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Compare_changes.png)

After making sure everything is correct, you can create the pull request. The owner of the repository can look at your request and decide to merge it (accepting your changes).

### Merging a Pull Request
![screenshot versions](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Versions_in_Git.png)

After a pull request has been made, the owner of a repository can merge a pull request to accept the changes that have been proposed by the maker of the request. Go to the pull request tab to see all the requests.

![screenshot Pull request tab](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Pull_request_tab.png)

Click on a pull request to see the changes that are proposed. There are separate tabs for conversation (comments on what has changed), Commits (where you can see the changes), and Files Changed (where you can see which files are affected and also the main changes).

![screenshot Files changed tab](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Files_changed.png)

Under conversation, if you wish to accept the changes you can press Merge pull request. If you are unsure you can comment, and if you wish to reject the pull request then you can use the Close pull request button.

![screenshot Close request](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Close_pull_request.png)

You will notice that GitHub has checked to make sure that the pull request does not conflict with any other code you have written in the main branch.

## Other Functionalities
### GitHub Pages
By adding an index.html file or a markdown file to your repository you can create your own webpage. By enabling GitHub pages within the settings of the repo GitHub will generate a webpage for you that can be shared online. The address of your repository could be, for example: [https://github.com/Francesca4242/SecretSanta](https://github.com/Francesca4242/SecretSanta). Once turned into a webpage, this will become: [http://francesca4242.github.io/SecretSanta](http://francesca4242.github.io/SecretSanta)

### Turning your GitHub Repository into a Website
Go back to your .html file and change the name of the file (whatever it is called) to
index.html. Upload this file to your repository by going to the repository page you just
created, clicking **add files** and then **upload files**.

![screenshot Upload files](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Upload_files2.png)

Upload the index.html file that you just renamed to the repository by dragging and dropping it into the area or navigating to the file in file explorer. Once done at the bottom type the changes you have made (for example ‘added index.html file) and press the green **commit changes** button.

![screenshot Commit changes](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Commit_changes2.png)

You should now be back at the repository main page, go to settings in the bar at the top on the right hand side. And then navigate to Pages in the side bar menu. 

![screenshot Settings pages](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/Settings_pages.png)

Second section down, select the source as main and click save.
Your game should then appear at the website on your pages (it may take a while to compile). GitHub pages creates a website address based on your GitHub username and the name of your repository. For example, this could be: https://[your_GitHub_username].github.io/[name_of_repository]

If you can't find it, then the page address should also be displayed on the screen, as below. 
![screenshot GitHub pages](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/GitHub_pages.png)

**Do not forget to share the link, so other people can have a look at it!**

### Projects
GitHub allows the functionality of creating projects to show workflows and collaborate. A project is an adaptable collection of items that you can view as a table, a kanban board, or a roadmap and that stays up-to-date with GitHub data. Your projects can track issues, pull requests, and ideas that you note down.

You can create and customise multiple views by filtering, sorting, and grouping issues and pull requests, visualise work with configurable charts, and add custom fields to track metadata specific to your team. Rather than enforcing a specific methodology, a project provides flexible features you can customise to your needs and processes.

You can find more information on starting a project [here](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project).

![screenshot GitHub projects](https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/GitHub_guide/GitHub_projects.png)

## Further Resources 

|Skill|Link|Comment|
|:----|:---|:------|
|Git|[https://www.w3schools.com/git/default.asp](https://www.w3schools.com/git/default.asp)|This is an online course by W3Schools on Git|
|GitHub|[https://github.com/skills/introduction-to-github](https://github.com/skills/introduction-to-github)|Tutorial on GitHub skills page|
|GitHub README files|[https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)|Explanation on GitHub README files: What are they and how to use them.|
|GitHub issues|[https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/quickstart](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/quickstart)|Quickstart for GitHub issues. Interactive guide to learn about GitHub issues.
|Markdown|[https://www.markdowntutorial.com/](https://www.markdowntutorial.com/)|Interactive tutorial about Markdown|
|Markdown|[https://www.youtube.com/watch?v=OXZ77HvL_Yg](https://www.youtube.com/watch?v=OXZ77HvL_Yg)|Video tutorial about Markdown|
|Markdown|[https://blog.webdevsimplified.com/2023-06/markdown-crash-course/](https://blog.webdevsimplified.com/2023-06/markdown-crash-course/)|Markdown crash course|
|Markdown|[https://dillinger.io/](https://dillinger.io/)| Online Markdown editor, to see how it works and to try it out!|
