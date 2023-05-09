import argparse 
from ricescheduler import make_url, sorted_classes, schedule, output, date_formats

parser = argparse.ArgumentParser()
parser.add_argument('semester', help='Spring or Fall')
parser.add_argument('year', type=int, help='Year as YYYY')
parser.add_argument('days', help='String of class days as MTWRF')
parser.add_argument('--verbose', action='store_true', help='Show cancelled classes in output')
args = parser.parse_args()

def check_args():
    checks = []
    checks.append(set(args.days + 'MTWRF') != set('MTWRF'))
    checks.append(args.semester.lower() not in ['spring','fall'])
    if True in checks:
        print 'Input error in your arguments.'
        parser.print_help()
        sys.exit(1)
    if args.year < 2009:
        print 'ERROR: The script only works for the years 2009 to the present.'
        sys.exit(1)

check_args()
url = make_url(args.semester, str(args.year))
day_index = {'M': 'Monday', 'T': 'Tuesday', 'W': 'Wednesday', 'R': 'Thursday', 'F': 'Friday'}
weekdays = [day_index[d] for d in args.days]
possible_classes, no_classes = sorted_classes(weekdays, url)
course = schedule(possible_classes, no_classes, show_no=True)
print course