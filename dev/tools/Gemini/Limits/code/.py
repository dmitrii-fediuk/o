from datetime import datetime, time, timedelta
import os
def calc(profiles, t_now):
	items = []
	t_end = t_now + timedelta(days=1)
	for p, t_base in profiles.items():
		diff = int((t_now - t_base).total_seconds())
		k = -(-diff // 18000)
		t_first = t_base + timedelta(hours=5 * k)
		times = []
		cur = t_first
		while t_end >= cur:
			times.append(cur.strftime('%H:%M'))
			cur += timedelta(hours=5)
		items.append((t_first, p, times))
	items.sort(key=lambda x: (x[0], x[1]))
	return '\n'.join([x[1] + ': ' + '\t'.join(x[2]) for x in items]) + '\n'
def main():
	dir_cur = os.path.dirname(os.path.abspath(__file__))
	path_ini = os.path.join(dir_cur, '.ini')
	path_res = os.path.join(dir_cur, '..', 'result', 'Limits.md')
	profiles = read_ini(path_ini)
	content = calc(profiles, datetime.now())
	write_result(path_res, content)
def read_ini(path):
	base_date = None
	profiles = {}
	with open(path, 'r', encoding='utf-8') as f:
		lines = f.readlines()
	for raw in lines:
		line = raw.strip()
		if '=' in line:
			k, v = [x.strip() for x in line.split('=', 1)]
			if 'date' == k:
				base_date = datetime.strptime(v.split()[0], '%Y-%m-%d').date()
			else:
				h, m = [int(x) for x in v.split(':')]
				profiles[k] = datetime.combine(base_date, time(h, m))
	return profiles
def write_result(path, content):
	os.makedirs(os.path.dirname(path), exist_ok=True)
	with open(path, 'w', encoding='utf-8') as f:
		f.write(content)
if '__main__' == __name__:
	main()
