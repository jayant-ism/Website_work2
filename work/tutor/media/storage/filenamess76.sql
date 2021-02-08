-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 24, 2021 at 12:22 PM
-- Server version: 5.7.32-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `work`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add country', 7, 'add_country'),
(26, 'Can change country', 7, 'change_country'),
(27, 'Can delete country', 7, 'delete_country'),
(28, 'Can view country', 7, 'view_country'),
(29, 'Can add state', 8, 'add_state'),
(30, 'Can change state', 8, 'change_state'),
(31, 'Can delete state', 8, 'delete_state'),
(32, 'Can view state', 8, 'view_state'),
(33, 'Can add class_details', 9, 'add_class_details'),
(34, 'Can change class_details', 9, 'change_class_details'),
(35, 'Can delete class_details', 9, 'delete_class_details'),
(36, 'Can view class_details', 9, 'view_class_details'),
(37, 'Can add connect', 10, 'add_connect'),
(38, 'Can change connect', 10, 'change_connect'),
(39, 'Can delete connect', 10, 'delete_connect'),
(40, 'Can view connect', 10, 'view_connect'),
(41, 'Can add connect_status', 11, 'add_connect_status'),
(42, 'Can change connect_status', 11, 'change_connect_status'),
(43, 'Can delete connect_status', 11, 'delete_connect_status'),
(44, 'Can view connect_status', 11, 'view_connect_status'),
(45, 'Can add designation', 12, 'add_designation'),
(46, 'Can change designation', 12, 'change_designation'),
(47, 'Can delete designation', 12, 'delete_designation'),
(48, 'Can view designation', 12, 'view_designation'),
(49, 'Can add language_list', 13, 'add_language_list'),
(50, 'Can change language_list', 13, 'change_language_list'),
(51, 'Can delete language_list', 13, 'delete_language_list'),
(52, 'Can view language_list', 13, 'view_language_list'),
(53, 'Can add level', 14, 'add_level'),
(54, 'Can change level', 14, 'change_level'),
(55, 'Can delete level', 14, 'delete_level'),
(56, 'Can view level', 14, 'view_level'),
(57, 'Can add rating', 15, 'add_rating'),
(58, 'Can change rating', 15, 'change_rating'),
(59, 'Can delete rating', 15, 'delete_rating'),
(60, 'Can view rating', 15, 'view_rating'),
(61, 'Can add user_details', 16, 'add_user_details'),
(62, 'Can change user_details', 16, 'change_user_details'),
(63, 'Can delete user_details', 16, 'delete_user_details'),
(64, 'Can view user_details', 16, 'view_user_details'),
(65, 'Can add user_login', 17, 'add_user_login'),
(66, 'Can change user_login', 17, 'change_user_login'),
(67, 'Can delete user_login', 17, 'delete_user_login'),
(68, 'Can view user_login', 17, 'view_user_login'),
(69, 'Can add skill', 18, 'add_skill'),
(70, 'Can change skill', 18, 'change_skill'),
(71, 'Can delete skill', 18, 'delete_skill'),
(72, 'Can view skill', 18, 'view_skill'),
(73, 'Can add message', 19, 'add_message'),
(74, 'Can change message', 19, 'change_message'),
(75, 'Can delete message', 19, 'delete_message'),
(76, 'Can view message', 19, 'view_message'),
(77, 'Can add messagewewqe', 20, 'add_messagewewqe'),
(78, 'Can change messagewewqe', 20, 'change_messagewewqe'),
(79, 'Can delete messagewewqe', 20, 'delete_messagewewqe'),
(80, 'Can view messagewewqe', 20, 'view_messagewewqe'),
(81, 'Can add message', 21, 'add_message'),
(82, 'Can change message', 21, 'change_message'),
(83, 'Can delete message', 21, 'delete_message'),
(84, 'Can view message', 21, 'view_message');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$Dj3n1wiOouy7$dmj1u5gf+0PZvNteoU8PwYtFNehBeutyo28lsOzvYgM=', '2021-01-19 14:39:20.207171', 1, 'jayant', '', '', '', 1, 1, '2021-01-16 07:29:00.232193');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `basic_class_details`
--

CREATE TABLE `basic_class_details` (
  `class_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `class_details` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `basic_connect`
--

CREATE TABLE `basic_connect` (
  `id` int(11) NOT NULL,
  `connect_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `connect_status` int(11) NOT NULL,
  `connect_seek_rating` int(11) NOT NULL,
  `connect_teach_rating` int(11) NOT NULL,
  `connect_rate` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `basic_connect_status`
--

CREATE TABLE `basic_connect_status` (
  `id` int(11) NOT NULL,
  `connect_status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `basic_designation`
--

CREATE TABLE `basic_designation` (
  `level` varchar(15) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `basic_level`
--

CREATE TABLE `basic_level` (
  `level` varchar(15) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `basic_message`
--

CREATE TABLE `basic_message` (
  `sender` varchar(1200) NOT NULL,
  `receiver` varchar(1200) NOT NULL,
  `message` varchar(1200) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `id` int(11) NOT NULL,
  `message_type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `basic_message`
--

INSERT INTO `basic_message` (`sender`, `receiver`, `message`, `timestamp`, `is_read`, `id`, `message_type`) VALUES
('1', '13', 'Lets see what happens', '2021-01-18 14:10:31.909645', 1, 1, 'text'),
('1', '13', 'Lets see what happenss', '2021-01-18 14:10:35.344670', 1, 2, 'text'),
('1', '13', 'media/storage/filenamess48.py', '2021-01-18 14:11:51.135547', 1, 3, 'file'),
('1', '13', 'media/storage/filenamess48.py', '2021-01-18 14:11:52.311528', 1, 4, 'text'),
('1', '13', 'media/storage/filenamess49.py', '2021-01-18 14:15:24.988709', 1, 5, 'file'),
('1', '13', 'media/storage/filenamess49.py', '2021-01-18 14:15:26.136291', 1, 6, 'text'),
('1', '13', 'media/storage/filenamess50.py', '2021-01-18 14:18:57.627475', 1, 7, 'file'),
('1', '13', 'media/storage/filenamess51.py', '2021-01-18 14:19:18.541141', 1, 8, 'file'),
('1', '13', 'media/storage/filenamess52.xlsx', '2021-01-18 14:26:30.563678', 1, 9, 'file');

-- --------------------------------------------------------

--
-- Table structure for table `basic_rating`
--

CREATE TABLE `basic_rating` (
  `rating` varchar(15) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `id` int(11) NOT NULL,
  `country` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `country`
--

INSERT INTO `country` (`id`, `country`) VALUES
(1, 'INDIA'),
(2, 'INDIA'),
(3, 'USA'),
(4, 'UAE');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-01-16 07:31:00.836162', '1', 'user_details object (1)', 1, '[{\"added\": {}}]', 16, 1),
(2, '2021-01-16 09:34:11.625549', '12', 'user_details object (12)', 1, '[{\"added\": {}}]', 16, 1),
(3, '2021-01-16 09:35:59.497762', '13', 'user_details object (13)', 1, '[{\"added\": {}}]', 16, 1),
(4, '2021-01-19 14:43:28.610740', '2', 'user_details object (2)', 1, '[{\"added\": {}}]', 16, 1),
(5, '2021-01-19 14:44:49.977008', '2', 'user_details object (2)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 16, 1),
(6, '2021-01-19 14:50:51.224480', '13', 'user_details object (13)', 2, '[{\"changed\": {\"fields\": [\"Seek skills\", \"Teach skills\"]}}]', 16, 1),
(7, '2021-01-19 14:50:55.743415', '13', 'user_details object (13)', 2, '[]', 16, 1),
(8, '2021-01-19 14:50:59.936317', '13', 'user_details object (13)', 2, '[]', 16, 1),
(9, '2021-01-19 14:51:06.408346', '12', 'user_details object (12)', 2, '[{\"changed\": {\"fields\": [\"Seek skills\", \"Teach skills\"]}}]', 16, 1),
(10, '2021-01-19 14:51:13.059643', '2', 'user_details object (2)', 2, '[]', 16, 1),
(11, '2021-01-19 14:51:18.933541', '1', 'user_details object (1)', 2, '[{\"changed\": {\"fields\": [\"Seek skills\", \"Teach skills\"]}}]', 16, 1),
(12, '2021-01-19 14:53:16.908897', '13', 'user_details object (13)', 2, '[{\"changed\": {\"fields\": [\"Seek skills\"]}}]', 16, 1),
(13, '2021-01-19 14:54:31.514571', '13', 'user_details object (13)', 2, '[]', 16, 1),
(14, '2021-01-19 14:54:59.262262', '13', 'user_details object (13)', 2, '[{\"changed\": {\"fields\": [\"Seek skills\"]}}]', 16, 1),
(15, '2021-01-19 14:55:09.646959', '13', 'user_details object (13)', 2, '[{\"changed\": {\"fields\": [\"Seek skills\"]}}]', 16, 1),
(16, '2021-01-19 14:55:20.179356', '13', 'user_details object (13)', 2, '[{\"changed\": {\"fields\": [\"Seek skills\"]}}]', 16, 1),
(17, '2021-01-19 14:55:51.427547', '13', 'user_details object (13)', 2, '[{\"changed\": {\"fields\": [\"Seek skills\"]}}]', 16, 1),
(18, '2021-01-19 15:06:27.527433', '13', 'user_details object (13)', 2, '[]', 16, 1),
(19, '2021-01-19 16:25:42.328633', '15', 'user_details object (15)', 1, '[{\"added\": {}}]', 16, 1),
(20, '2021-01-19 16:27:20.401909', '16', 'user_details object (16)', 1, '[{\"added\": {}}]', 16, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(9, 'basic', 'class_details'),
(10, 'basic', 'connect'),
(11, 'basic', 'connect_status'),
(7, 'basic', 'country'),
(12, 'basic', 'designation'),
(13, 'basic', 'language_list'),
(14, 'basic', 'level'),
(21, 'basic', 'message'),
(15, 'basic', 'rating'),
(18, 'basic', 'skill'),
(8, 'basic', 'state'),
(16, 'basic', 'user_details'),
(17, 'basic', 'user_login'),
(19, 'chat', 'message'),
(20, 'chat', 'messagewewqe'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-01-16 07:27:38.387973'),
(2, 'auth', '0001_initial', '2021-01-16 07:27:38.835823'),
(3, 'admin', '0001_initial', '2021-01-16 07:27:40.278989'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-01-16 07:27:40.629623'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-01-16 07:27:40.661222'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-01-16 07:27:40.952896'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-01-16 07:27:41.006010'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-01-16 07:27:41.041190'),
(9, 'auth', '0004_alter_user_username_opts', '2021-01-16 07:27:41.070420'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-01-16 07:27:41.193600'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-01-16 07:27:41.202252'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-01-16 07:27:41.232459'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-01-16 07:27:41.262288'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-01-16 07:27:41.292928'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-01-16 07:27:41.324841'),
(16, 'auth', '0011_update_proxy_permissions', '2021-01-16 07:27:41.358533'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-01-16 07:27:41.383854'),
(18, 'basic', '0001_initial', '2021-01-16 07:27:41.402610'),
(19, 'basic', '0002_class_details_connect_connect_status_designation_language_list_level_rating_skill_user_details_user_', '2021-01-16 07:27:42.105688'),
(20, 'sessions', '0001_initial', '2021-01-16 07:27:42.335864'),
(21, 'basic', '0003_auto_20210116_0935', '2021-01-16 09:35:15.007016'),
(22, 'basic', '0004_auto_20210116_0944', '2021-01-16 09:44:09.809852'),
(23, 'basic', '0005_delete_state', '2021-01-16 09:45:30.642218'),
(24, 'basic', '0006_delete_country', '2021-01-16 09:49:35.418413'),
(25, 'basic', '0007_country', '2021-01-16 09:50:04.228223'),
(26, 'basic', '0008_message', '2021-01-18 14:08:58.593876');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ej7pmrim7qtn3b64wkjq1p54psktcyyj', '.eJxVjr0OAiEQhN-F2hBg-bW09xkICyinBpLjrjK-u5BcodlmsjPzZd7Eh30rfu959UsiZ8LJ6feHIT5znUZ6hHpvNLa6rQvSGaGH2-m1pfy6HNk_QAm9jDZgZKgZSLxx45JiCiw6niRIZwVIMAbA2SyYYyxoHBK5iFzbDGrcgE7cnMjF5wtOpjm6:1l3izd:xyswlRAjuHKOkrU_fDL7T9Sxy2ATLuJ2FPVp9kXZKms', '2021-02-07 17:16:05.670692'),
('ym0sdjgiupohl163gwweisnx160p4wzq', '.eJxVjr0OAiEQhN-F2hBg-bW09xkICyinBpLjrjK-u5BcodlmsjPzZd7Eh30rfu959UsiZ8LJ6feHIT5znUZ6hHpvNLa6rQvSGaGH2-m1pfy6HNk_QAm9jDZgZKgZSLxx45JiCiw6niRIZwVIMAbA2SyYYyxoHBK5iFzbDGrcgE7cnMg_XxU3OYg:1l1uyt:uEzvUEL58OAGa2sd91oGqocagUEr93Fi4G-PD7RQRFA', '2021-02-02 17:39:51.508749');

-- --------------------------------------------------------

--
-- Table structure for table `language_list`
--

CREATE TABLE `language_list` (
  `id` int(11) NOT NULL,
  `language` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Message`
--

CREATE TABLE `Message` (
  `sender` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `skill`
--

CREATE TABLE `skill` (
  `id` int(11) NOT NULL,
  `skill_name` varchar(45) DEFAULT NULL,
  `skill_description` varchar(45) DEFAULT NULL,
  `skills` json NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int(11) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `phone` decimal(10,0) NOT NULL,
  `address` varchar(15) NOT NULL,
  `role` int(11) NOT NULL,
  `seek_designation` varchar(15) NOT NULL,
  `teach_designation` varchar(15) NOT NULL,
  `seek_skills` json NOT NULL,
  `teach_skills` json NOT NULL,
  `country` varchar(45) NOT NULL,
  `rate` decimal(5,4) NOT NULL,
  `rating` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `language` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`id`, `first_name`, `last_name`, `phone`, `address`, `role`, `seek_designation`, `teach_designation`, `seek_skills`, `teach_skills`, `country`, `rate`, `rating`, `level`, `image`, `language`) VALUES
(1, 'Jayant', 'Anand', '2133123123', 'asdads', 1, 'adsdas', 'sadasdasda', '{\"skills\": [\"Django\", \"C++\"]}', '{\"skills\": [\"Django\", \"C++\"]}', 'India', '1.0000', 1, 1, '', 'ENGLISH'),
(2, 'Aman', 'Kumar', '6203200626', 'asdads', 1, 'Webdesign', 'null', '{\"skills\": [\"Django\", \"C++\"]}', '{\"skills\": [\"Django\", \"C++\"]}', 'India', '1.0000', 3, 1, 'profile_images/Test526.jpg', 'ENGLISH'),
(12, 'Jayant', 'Anand', '1123112', 'asdads', 2, 'asdadasdad', 'sadasdasda', '{\"skills\": [\"Django\", \"C++\"]}', '{\"skills\": [\"Django\", \"C++\"]}', 'India', '1.0000', 3, 1, '', 'ENGLISH'),
(13, 'Jayant', 'Anand', '21313', 'asdads', 2, 'asdadasdad', 'sadasdasda', '{\"skills\": [\"Django\", \"C++\"]}', '{\"skills\": [\"Django\", \"C++\"]}', 'India', '1.0000', 4, 1, '', 'ENGLISH'),
(15, 'we', 'Kumar', '2433423', 'Random', 1, 'Webdesign', 'Coding', '{\"skills\": [\"Django\", \"C++\"]}', '{\"skills\": [\"Django\", \"C++\"]}', 'India', '1.0000', 5, 4, '', 'ENGLISH'),
(16, 'weqw', 'Kumarqwe', '132213', 'Random', 1, 'Webdesign', 'Coding', '{\"skills\": [\"Django\", \"C\"]}', '{\"skills\": [\"Django\", \"C++\"]}', 'India', '1.0000', 5, 4, '', 'HINDI');

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--

CREATE TABLE `user_login` (
  `id` int(11) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `email_id` varchar(15) NOT NULL,
  `pwd` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `basic_class_details`
--
ALTER TABLE `basic_class_details`
  ADD PRIMARY KEY (`class_id`);

--
-- Indexes for table `basic_connect`
--
ALTER TABLE `basic_connect`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `basic_connect_status`
--
ALTER TABLE `basic_connect_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `basic_designation`
--
ALTER TABLE `basic_designation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `basic_level`
--
ALTER TABLE `basic_level`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `basic_message`
--
ALTER TABLE `basic_message`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `basic_rating`
--
ALTER TABLE `basic_rating`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `language_list`
--
ALTER TABLE `language_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `skill`
--
ALTER TABLE `skill`
  ADD PRIMARY KEY (`id`),
  ADD KEY `skill_user_id_28aecfd4_fk_user_details_id` (`user_id`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_login`
--
ALTER TABLE `user_login`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `basic_connect`
--
ALTER TABLE `basic_connect`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `basic_message`
--
ALTER TABLE `basic_message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `country`
--
ALTER TABLE `country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT for table `language_list`
--
ALTER TABLE `language_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `skill`
--
ALTER TABLE `skill`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `skill`
--
ALTER TABLE `skill`
  ADD CONSTRAINT `skill_user_id_28aecfd4_fk_user_details_id` FOREIGN KEY (`user_id`) REFERENCES `user_details` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
