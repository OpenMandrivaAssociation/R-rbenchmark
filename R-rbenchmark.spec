%global packname  rbenchmark
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.3
Release:          1
Summary:          Benchmarking routine for R
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
rbenchmark is inspired by the Perl module Benchmark, and is intended to
facilitate benchmarking of arbitrary R code. The library consists of just
one function, benchmark, which is a simple wrapper around system.time. 
Given a specification of the benchmarking process (counts of replications,
evaluation environment) and an arbitrary number of expressions, benchmark
evaluates each of the expressions in the specified environment,
replicating the evaluation as many times as specified, and returning the
results conveniently wrapped into a data frame.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 776463
- Import R-rbenchmark
- Import R-rbenchmark

