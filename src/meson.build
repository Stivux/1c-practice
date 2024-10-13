pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'calories'
gnome = import('gnome')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'calories.in',
  output: 'calories',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr-xr-x'
)


calories_sources = [
  '__init__.py',
  'main.py',
  'calories_item.py',
  'window.py',
  'backend/db.py',
  'backend/_constants.py',
  'backend/_pathes.py',
  'backend/_dish.py'
]

install_data(calories_sources, install_dir: moduledir)
