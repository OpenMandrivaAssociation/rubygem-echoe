%define oname echoe

Summary:    A Rubygems packaging tool
Name:       rubygem-%{oname}
Version:    4.5.5
Release:    %mkrel 1
Group:      Development/Ruby
License:    MIT
URL:        http://blog.evanweaver.com/files/doc/fauna/echoe/
Source0:    http://gems.rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(gemcutter)
Requires:   rubygem(rubyforge)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A Rubygems packaging tool that provides Rake tasks for documentation,
extension compiling, testing, and deployment.

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/echoe.gemspec

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/vendor/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/MIT-LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/lib/echoe.rb
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/lib/echoe/extensions.rb
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/lib/echoe/platform.rb
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/lib/echoe/rubygems.rb
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
