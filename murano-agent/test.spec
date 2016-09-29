%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}
%global pypi_name cinder

Name:             openstack-cinder
# Liberty semver reset
# https://review.openstack.org/#/q/I6a35fa0dda798fad93b804d00a46af80f08d475c,n,z
Epoch:            1
Version:          XXX
Release:          XXX
Summary:          OpenStack Volume service

License:          ASL 2.0
URL:              http://www.openstack.org/software/openstack-storage/
Source0:          https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz

Source1:          cinder-dist.conf
Source2:          cinder.logrotate

Source10:         openstack-cinder-api.service
Source11:         openstack-cinder-scheduler.service
Source12:         openstack-cinder-volume.service
Source13:         openstack-cinder-backup.service
Source20:         cinder-sudoers


BuildArch:        noarch
BuildRequires:    intltool
BuildRequires:    python-d2to1
BuildRequires:    python-oslo-sphinx
BuildRequires:    python-pbr
BuildRequires:    python-reno
BuildRequires:    python-sphinx
BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-netaddr
BuildRequires:    systemd
BuildRequires:    git
BuildRequires:    os-brick
BuildRequires:    pyparsing
BuildRequires:    pytz
BuildRequires:    python-decorator
# Required to build cinder.conf
BuildRequires:    python-google-api-client >= 1.4.2
BuildRequires:    python-keystonemiddleware
BuildRequires:    python-glanceclient >= 1:2.0.0
BuildRequires:    python-novaclient >= 2.29.0
BuildRequires:    python-swiftclient >= 2.2.0
BuildRequires:    python-oslo-db
BuildRequires:    python-oslo-config >= 2:3.7.0
BuildRequires:    python-oslo-policy
BuildRequires:    python-oslo-reports
BuildRequires:    python-oslotest
BuildRequires:    python-oslo-utils
BuildRequires:    python-oslo-versionedobjects
BuildRequires:    python-oslo-vmware
BuildRequires:    python-os-win
BuildRequires:    python-castellan
BuildRequires:    python-crypto
BuildRequires:    python-lxml
BuildRequires:    python-osprofiler
BuildRequires:    python-paramiko
BuildRequires:    python-suds
BuildRequires:    python-taskflow
BuildRequires:    python-tooz
BuildRequires:    python-oslo-log
BuildRequires:    python-oslo-i18n
BuildRequires:    python-barbicanclient
BuildRequires:    python-requests
BuildRequires:    python-retrying

# Required to compile translation files
BuildRequires:    python-babel

Requires:         python-cinder = %{epoch}:%{version}-%{release}

# we dropped the patch to remove PBR for Delorean
Requires:         python-pbr

# as convenience
Requires:         python-cinderclient

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires(pre):    shadow-utils

Requires:         lvm2
Requires:         python-osprofiler
Requires:         python-rtslib

%description
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.


%package -n       python-cinder
Summary:          OpenStack Volume Python libraries
Group:            Applications/System

Requires:         sudo

Requires:         qemu-img
Requires:         sysfsutils
Requires:         os-brick
Requires:         python-paramiko

Requires:         python-castellan
Requires:         python-eventlet
Requires:         python-greenlet
Requires:         python-iso8601 >= 0.1.9
Requires:         python-lxml
Requires:         python-anyjson
Requires:         python-stevedore
Requires:         python-suds
Requires:         python-tooz

Requires:         python-sqlalchemy
Requires:         python-migrate

Requires:         python-paste-deploy
Requires:         python-routes
Requires:         python-webob

Requires:         python-glanceclient >= 1:2.0.0
Requires:         python-swiftclient >= 2.2.0
Requires:         python-keystoneclient
Requires:         python-novaclient >= 1:2.29.0

Requires:         python-oslo-config >= 2:3.7.0
Requires:         python-six >= 1.9.0
Requires:         python-psutil >= 1.1.1

Requires:         python-babel
Requires:         python-google-api-client >= 1.4.2

Requires:         python-oslo-rootwrap
Requires:         python-oslo-utils
Requires:         python-oslo-serialization
Requires:         python-oslo-db
Requires:         python-oslo-context
Requires:         python-oslo-concurrency
Requires:         python-oslo-middleware
Requires:         python-taskflow
Requires:         python-oslo-messaging >= 4.0.0
Requires:         python-oslo-policy >= 0.5.0
Requires:         python-oslo-reports
Requires:         python-oslo-service
Requires:         python-oslo-versionedobjects

Requires:         iscsi-initiator-utils

Requires:         python-osprofiler

Requires:         python-httplib2 >= 0.7.5
Requires:         python-oauth2client >= 1.5.0

Requires:         python-oslo-log
Requires:         python-oslo-i18n
Requires:         python-barbicanclient
Requires:         python-requests
Requires:         python-retrying
Requires:         pyparsing
Requires:         pytz
Requires:         python-decorator


%description -n   python-cinder
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains the cinder Python library.

%package -n python-cinder-tests
Summary:        Cinder tests
Requires:       openstack-cinder = %{epoch}:%{version}-%{release}

# Added test requirements
Requires:       python-hacking
Requires:       python-anyjson
Requires:       python-coverage
Requires:       python-ddt
Requires:       python-fixtures
Requires:       python-mock
Requires:       python-mox3
Requires:       python-oslotest
Requires:       python-subunit
Requires:       python-testtools
Requires:       python-testrepository
Requires:       python-testresources
Requires:       python-testscenarios
Requires:       python-os-testr
Requires:       python-tempest-lib

%description -n python-cinder-tests
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains the Cinder test files.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Volume
Group:            Documentation

Requires:         %{name} = %{epoch}:%{version}-%{release}

BuildRequires:    graphviz

# Required to build module documents
BuildRequires:    python-eventlet
BuildRequires:    python-routes
BuildRequires:    python-sqlalchemy
BuildRequires:    python-webob
# while not strictly required, quiets the build down when building docs.
BuildRequires:    python-migrate
BuildRequires:    python-iso8601 >= 0.1.9

%description      doc
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains documentation files for cinder.
%endif

%prep
%autosetup -n cinder-%{upstream_version} -S git

find . \( -name .gitignore -o -name .placeholder \) -delete

find cinder -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i 's/%{version}.%{milestone}/%{version}/' PKG-INFO

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires


%build
# Generate config file
PYTHONPATH=. oslo-config-generator --config-file=cinder/config/cinder-config-generator.conf

# Build
%{__python2} setup.py build

# Generate i18n files
%{__python2} setup.py compile_catalog -d build/lib/%{pypi_name}/locale

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

%if 0%{?with_doc}
%{__python2} setup.py build_sphinx --builder html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%{__python2} setup.py build_sphinx --builder man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/cinder
install -d -m 755 %{buildroot}%{_sharedstatedir}/cinder/tmp
install -d -m 755 %{buildroot}%{_localstatedir}/log/cinder

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/cinder
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_datadir}/cinder/cinder-dist.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/cinder/volumes
install -p -D -m 640 etc/cinder/rootwrap.conf %{buildroot}%{_sysconfdir}/cinder/rootwrap.conf
install -p -D -m 640 etc/cinder/api-paste.ini %{buildroot}%{_sysconfdir}/cinder/api-paste.ini
install -p -D -m 640 etc/cinder/policy.json %{buildroot}%{_sysconfdir}/cinder/policy.json
install -p -D -m 640 etc/cinder/cinder.conf.sample %{buildroot}%{_sysconfdir}/cinder/cinder.conf

# Install initscripts for services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/openstack-cinder-api.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/openstack-cinder-scheduler.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/openstack-cinder-volume.service
install -p -D -m 644 %{SOURCE13} %{buildroot}%{_unitdir}/openstack-cinder-backup.service

# Install sudoers
install -p -D -m 440 %{SOURCE20} %{buildroot}%{_sysconfdir}/sudoers.d/cinder

# Install logrotate
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-cinder

# Install pid directory
install -d -m 755 %{buildroot}%{_localstatedir}/run/cinder

# Install rootwrap files in /usr/share/cinder/rootwrap
mkdir -p %{buildroot}%{_datarootdir}/cinder/rootwrap/
install -p -D -m 644 etc/cinder/rootwrap.d/* %{buildroot}%{_datarootdir}/cinder/rootwrap/


# Symlinks to rootwrap config files
mkdir -p %{buildroot}%{_sysconfdir}/cinder/rootwrap.d
for filter in %{_datarootdir}/os-brick/rootwrap/*.filters; do
ln -s $filter %{buildroot}%{_sysconfdir}/cinder/rootwrap.d/
done

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python2_sitelib}/%{pypi_name}/locale/*/LC_*/%{pypi_name}*po
rm -f %{buildroot}%{python2_sitelib}/%{pypi_name}/locale/*pot
mv %{buildroot}%{python2_sitelib}/%{pypi_name}/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang %{pypi_name} --all-name

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/cinder-all
rm -f %{buildroot}%{_bindir}/cinder-debug
rm -fr %{buildroot}%{python2_sitelib}/run_tests.*
rm -f %{buildroot}/usr/share/doc/cinder/README*

%pre
getent group cinder >/dev/null || groupadd -r cinder --gid 165
if ! getent passwd cinder >/dev/null; then
  useradd -u 165 -r -g cinder -G cinder,nobody -d %{_sharedstatedir}/cinder -s /sbin/nologin -c "OpenStack Cinder Daemons" cinder
fi
exit 0

%post
%systemd_post openstack-cinder-volume
%systemd_post openstack-cinder-api
%systemd_post openstack-cinder-scheduler
%systemd_post openstack-cinder-backup

%preun
%systemd_preun openstack-cinder-volume
%systemd_preun openstack-cinder-api
%systemd_preun openstack-cinder-scheduler
%systemd_preun openstack-cinder-backup

%postun
%systemd_postun_with_restart openstack-cinder-volume
%systemd_postun_with_restart openstack-cinder-api
%systemd_postun_with_restart openstack-cinder-scheduler
%systemd_postun_with_restart openstack-cinder-backup

%files
%dir %{_sysconfdir}/cinder
%config(noreplace) %attr(-, root, cinder) %{_sysconfdir}/cinder/cinder.conf
%config(noreplace) %attr(-, root, cinder) %{_sysconfdir}/cinder/api-paste.ini
%config(noreplace) %attr(-, root, cinder) %{_sysconfdir}/cinder/rootwrap.conf
%config(noreplace) %attr(-, root, cinder) %{_sysconfdir}/cinder/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-cinder
%config(noreplace) %{_sysconfdir}/sudoers.d/cinder
%{_sysconfdir}/cinder/rootwrap.d/
%attr(-, root, cinder) %{_datadir}/cinder/cinder-dist.conf

%dir %attr(0750, cinder, root) %{_localstatedir}/log/cinder
%dir %attr(0755, cinder, root) %{_localstatedir}/run/cinder
%dir %attr(0755, cinder, root) %{_sysconfdir}/cinder/volumes

%{_bindir}/cinder-*
%{_unitdir}/*.service
%{_datarootdir}/cinder
%{_mandir}/man1/cinder*.1.gz

%defattr(-, cinder, cinder, -)
%dir %{_sharedstatedir}/cinder
%dir %{_sharedstatedir}/cinder/tmp

%files -n python-cinder -f %{pypi_name}.lang
%{?!_licensedir: %global license %%doc}
%license LICENSE
%{python2_sitelib}/cinder
%{python2_sitelib}/cinder-*.egg-info
%exclude %{python2_sitelib}/cinder/tests

%files -n python-cinder-tests
%license LICENSE
%{python2_sitelib}/cinder/tests

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%endif

%changelog