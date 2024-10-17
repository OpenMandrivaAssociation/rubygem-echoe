# Generated from echoe-4.5.5.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	echoe

Summary:	Rubygems packaging tool
Name:		rubygem-%{rbname}

Version:	4.5.5
Release:	3
Group:		Development/Ruby
License:	MIT
URL:		https://fauna.github.com/fauna/echoe/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems >= 1.2
BuildArch:	noarch

%description
A Rubygems packaging tool that provides Rake tasks for documentation,
extension compiling, testing, and deployment.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f vendor/

%install
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/echoe
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/vendor/
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/vendor/rake
%{ruby_gemdir}/gems/%{rbname}-%{version}/vendor/rake/MIT-LICENSE
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/vendor/rake/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/vendor/rake/lib/rake
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/vendor/rake/lib/rake/contrib
%{ruby_gemdir}/gems/%{rbname}-%{version}/vendor/rake/lib/rake/contrib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/echoe/*.rb
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Tue Mar 15 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.5.5-1
+ Revision: 645111
- regenerate spec with gem2rpm5
- new release: 4.5.5

* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 4.3.1-1mdv2011.0
+ Revision: 584413
- import rubygem-echoe

