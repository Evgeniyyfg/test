init python:
    
    event('morale_below_50', triggers='week_end', conditions=('castle.morale < 50','castle.morale > 45'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_45', triggers='week_end', conditions=('castle.morale < 45','castle.morale > 40'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_40_1', triggers='week_end', conditions=('castle.morale < 40','castle.morale > 35'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_40_2', triggers='week_end', conditions=('castle.morale < 40','castle.morale > 35'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_35_1', triggers='week_end', conditions=('castle.morale < 35','castle.morale > 30'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_35_2', triggers='week_end', conditions=('castle.morale < 35','castle.morale > 30'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_30_1', triggers='week_end', conditions=('castle.morale < 30','castle.morale > 25'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_30_2', triggers='week_end', conditions=('castle.morale < 30','castle.morale > 25'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_25_1', triggers='week_end', conditions=('castle.morale < 25','castle.morale > 20'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_25_2', triggers='week_end', conditions=('castle.morale < 25','castle.morale > 20'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_20_1', triggers='week_end', conditions=('castle.morale < 20','castle.morale > 15'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_20_2', triggers='week_end', conditions=('castle.morale < 20','castle.morale > 15'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_15_1', triggers='week_end', conditions=('castle.morale < 15','castle.morale > 0'), group='low_morale_event', run_count=1, priority=pr_warning)
    event('morale_below_15_2', triggers='week_end', conditions=('castle.morale < 15','castle.morale > 0'), group='low_morale_event', run_count=1, priority=pr_warning)

label morale_below_50:
    "Morale below 50"

label morale_below_45:
    "Morale below 45"

label morale_below_40_1:
    "Morale below 40 #1"

label morale_below_40_2:
    "Morale below 40 #2"

label morale_below_35_1:
    "Morale below 35 #1"

label morale_below_35_2:
    "Morale below 35 #2"

label morale_below_30_1:
    "Morale below 30 #1"

label morale_below_30_2:
    "Morale below 30 #2"

label morale_below_25_1:
    "Morale below 25 #1"

label morale_below_25_2:
    "Morale below 25 #2"

label morale_below_20_1:
    "Morale below 20 #1"

label morale_below_20_2:
    "Morale below 20 #2"

label morale_below_15_1:
    "Morale below 15 #1"

label morale_below_15_2:
    "Morale below 15 #2"
