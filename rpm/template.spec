%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-hfl-driver
Version:        0.0.16
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS hfl_driver package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-angles
Requires:       ros-noetic-camera-info-manager
Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-image-transport
Requires:       ros-noetic-message-generation
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-udp-com
Requires:       ros-noetic-visualization-msgs
BuildRequires:  ros-noetic-angles
BuildRequires:  ros-noetic-camera-info-manager
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-image-transport
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf2
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-udp-com
BuildRequires:  ros-noetic-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The hfl package

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Aug 28 2020 Evan Flynn <evan.flynn@continental.com> - 0.0.16-1
- Autogenerated by Bloom

* Fri Aug 28 2020 Evan Flynn <evan.flynn@continental.com> - 0.0.15-1
- Autogenerated by Bloom

* Fri Aug 28 2020 Evan Flynn <evan.flynn@continental.com> - 0.0.14-1
- Autogenerated by Bloom

* Mon Aug 24 2020 Evan Flynn <evan.flynn@continental.com> - 0.0.12-1
- Autogenerated by Bloom

