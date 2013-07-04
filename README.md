rpm-gperftools
==============

An RPM spec file to build and install the Google Perftools.

To Build: 

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`sudo yum -y install libunwind-devel`

`wget https://gperftools.googlecode.com/files/gperftools-2.0.tar.gz -O ~/rpmbuild/SOURCES/gperftools-2.0.tar.gz`

`wget https://raw.github.com/nmilford/rpm-gperftools/master/gperftools.spec -O ~/rpmbuild/SPECS/gperftools.spec`

`rpmbuild -bb ~/rpmbuild/SPECS/gperftools.spec`
