%global milestone 0rc1
%{!?upstream_version: %global upstream_version %{version}.%{?milestone}}

Name:             murano-agent
Version:          3.0.0
Release:          0.1.rc1%{?dist}
Summary:          VM-side guest agent that accepts commands from Murano engine and executes them.
License:          ASL 2.0
URL:              http://git.openstack.org/cgit/openstack/%{name}
Source0:          http://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
Source10:         murano-agent.service
Source11:         murano-agent.logrotate

BuildArch:        noarch

# delete after test
BuildRequires:  gettext
BuildRequires:  python-beautifulsoup4
BuildRequires:  python-mock
BuildRequires:  python-mox3


BuildRequires:    python-devel
BuildRequires:    python-pbr >= 1.6
BuildRequires:    python-nose
BuildRequires:    python-setuptools
BuildRequires:    python-sphinx >= 1.1.2
BuildRequires:    python-oslo-config >= 2:3.14.0
BuildRequires:    python-oslo-log >= 1.14.0
BuildRequires:    python-oslo-service >= 1.10.0
BuildRequires:    python-oslo-utils >= 3.16.0
BuildRequires:    systemd-units

Requires:         python-pbr >= 1.6
Requires:         python-six >= 1.9.0
Requires:         python-oslo-config >= 2:3.14.0
Requires:         python-oslo-log >= 1.14.0
Requires:         python-oslo-service >= 1.10.0
Requires:         python-oslo-utils >= 3.16.0
Requires:         python-requests >= 2.10.0
Requires:         python-anyjson >= 0.3.3
Requires:         python-eventlet >= 0.18.2
Requires:         GitPython >= 1.0.1
Requires:         PyYAML >= 3.1.0
Requires:         python-semantic-version
Requires:         python-kombu >= 3.0.25

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd



%description
Murano Agent is the VM-side guest agent that accepts commands from Murano engine and executes them.

%prep
%setup -q -n %{name}-%{upstream_version}

# Let RPM handle the dependencies
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%py2_build
# Generate configuration files
PYTHONPATH=. oslo-config-generator --config-file etc/oslo-config-generator/muranoagent.conf

# generate html docs
# ls -R
# $(pwd)
# export OSLO_PACKAGE_VERSION=%{upstream_version}
# %{__python2} setup.py --verbose build_sphinx --verbose
# remove the sphinx-build leftovers
# rm -rf doc/build/html/.{doctrees,buildinfo}
# $(pwd)

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# Install conf file
install -p -D -m 644 etc/muranoagent/muranoagent.conf.sample %{buildroot}%{_sysconfdir}/murano-agent/muranoagent.conf

# Install initscript for services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/murano-agent.service

# Install logrotate
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/logrotate.d/murano-agent

# Install log directory
install -d -m 755 %{buildroot}%{_localstatedir}/log/murano-agent

#install working directory for daemon
install -d -m 755 %{buildroot}%{_sharedstatedir}/murano-agent

%post
%systemd_post murano-agent

%preun
%systemd_preun murano-agent

%postun
%systemd_postun_with_restart murano-agent



%files
%license LICENSE
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/logrotate.d/murano-agent
%config(noreplace) %{_sysconfdir}/murano-agent/muranoagent.conf
%{_bindir}/muranoagent
%{_unitdir}/murano-agent.service
%dir %attr(0750, root, root) %{_localstatedir}/log/murano-agent
%dir %{_sharedstatedir}/murano-agent
%{python2_sitelib}/muranoagent
%{python2_sitelib}/murano_agent-*.egg-info


%changelog
* Mon Sep 19 2016 Andrii Kroshchenko <akroshchenko@mirantis.com> - 3.0.0.0rc1
- Initial commit
