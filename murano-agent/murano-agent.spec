%global milestone 0rc1
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:             murano-agent
Version:          3.0.0
Release:          0.1%{?milestone}%{?dist}
Summary:          VM-side guest agent that accepts commands from Murano engine and executes them.
License:          ASL 2.0
URL:              http://git.openstack.org/cgit/openstack/%{name}
Source0:          https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
Source1:          murano-agent.service
Source2:          murano-agent.logrotate

BuildArch:        noarch


BuildRequires:    python-devel
BuildRequires:    python-pbr >= 1.6
BuildRequires:    python-setuptools
BuildRequires:    python-sphinx >= 1.2.1
BuildRequires:    python-oslo-config >= 2:3.14.0
BuildRequires:    python-oslo-log >= 3.11.0
BuildRequires:    python-oslo-service >= 1.10.0
BuildRequires:    python-oslo-utils >= 3.16.0
# test requirements
BuildRequires:    python-kombu >= 3.0.25
BuildRequires:    python-anyjson >= 0.3.3
BuildRequires:    python-semantic-version
BuildRequires:    GitPython >= 1.0.1
BuildRequires:    python2-hacking >= 0.10.0
BuildRequires:    python-unittest2
BuildRequires:    python-coverage >= 3.6
BuildRequires:    python-mock >= 2.0
BuildRequires:    python-testtools >= 1.4.0
BuildRequires:    python-testrepository >= 0.0.18
# doc build requirements
BuildRequires:    python-oslo-sphinx >= 2.5.0
BuildRequires:    python-sphinx >= 1.2.1
BuildRequires:    python2-reno >= 1.8.0

BuildRequires:    systemd-units

Requires:         python-pbr >= 1.6
Requires:         python-six >= 1.9.0
Requires:         python-oslo-config >= 2:3.14.0
Requires:         python-oslo-log >= 3.11.0
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
export OSLO_PACKAGE_VERSION=%{upstream_version}
%{__python2} setup.py build_sphinx

# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# Install conf file
install -p -D -m 644 etc/muranoagent/muranoagent.conf.sample %{buildroot}%{_sysconfdir}/murano-agent/muranoagent.conf

# Install initscript for services
install -p -D -m 644 %{Source1} %{buildroot}%{_unitdir}/murano-agent.service

# Install logrotate
install -p -D -m 644 %{Source2} %{buildroot}%{_sysconfdir}/logrotate.d/murano-agent

# Install log directory
install -d -m 755 %{buildroot}%{_localstatedir}/log/murano-agent

#install working directory for daemon
install -d -m 755 %{buildroot}%{_sharedstatedir}/murano-agent

%check
export PYTHONPATH="%{python2_sitearch}:%{python2_sitelib}:%{buildroot}%{python2_sitelib}"
%{__python2} setup.py testr --coverage --testr-args='{posargs}'


%post
%systemd_post murano-agent

%preun
%systemd_preun murano-agent

%postun
%systemd_postun_with_restart murano-agent



%files
%license LICENSE
%doc README.rst
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
