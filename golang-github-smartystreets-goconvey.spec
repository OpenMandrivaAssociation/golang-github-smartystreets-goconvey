# https://github.com/smartystreets/goconvey
%global goipath         github.com/smartystreets/goconvey
%global commit          ef6db91d284a0e7badaa1f0c404c30aa7dee3aed

%gometa

Name:           %{goname}
Version:        1.6.3
Release:        1%{?dist}
Summary:        Behavioral testing in the browser, integrates with go test
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/jtolds/gls)
BuildRequires: golang(github.com/smartystreets/assertions)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
# This test fails with latest smartystreets/assertions 
%gochecks -d convey/reporting -d web/server/watch


%files devel -f devel.file-list
%license LICENSE.md
%doc README.md CONTRIBUTING.md


%changelog
* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.3-1.20181006gitef6db91
- Bump to commit ef6db91d284a0e7badaa1f0c404c30aa7dee3aed

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-0.8.gitbf58a9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-0.7.gitbf58a9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-0.6.gitbf58a9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-0.5.gitbf58a9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-0.4.gitbf58a9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.6.1-0.3.gitbf58a9a
- Polish the spec file
  related: #1250511

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-0.2.gitbf58a9a
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Apr 14 2016 jchaloup <jchaloup@redhat.com> - 1.6.1-0.1.gitbf58a9a
- Bump to upstream bf58a9a1291224109919756b4dcc469c670cc7e4
  Polish the spec file
  related: #1250511

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git43652d6
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git43652d6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git43652d6
- Add missing BRs
  related: #1250511

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git43652d6
- Update spec file to spec-2.0
  resolves: #1250511

* Thu Apr 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git43652d6
- First package for Fedora
  resolves: #1214862
