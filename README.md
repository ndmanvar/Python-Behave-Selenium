
Setup:

In the command line you need to input the environmental variables for your Sauce Labs username and access key:

  $ export SAUCE_USERNAME=your_username
  $ export SAUCE_ACCESS_KEY=your_access_key

To run the tests, cd into the testchallenge directory and enter:

  $ behave-parallel/bin/behave --processes 12 --parallel-element scenario