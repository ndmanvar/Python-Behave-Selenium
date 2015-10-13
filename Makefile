run_all_in_parallel:
	make -j test_XP_chrome_43 test_Windows7_firefox_33 

test_XP_chrome_43:
	platform=XP browserName=chrome version=43.0 \
		behave-parallel/bin/behave --processes 12 --parallel-element scenario

test_Windows7_firefox_33:
	platform="Windows 7" browserName=firefox version=33.0 \
		behave-parallel/bin/behave --processes 12 --parallel-element scenario