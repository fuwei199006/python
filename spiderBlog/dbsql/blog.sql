/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50611
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50611
File Encoding         : 65001

Date: 2016-01-06 18:13:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for blog
-- ----------------------------
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog` (
  `blogId` int(11) NOT NULL AUTO_INCREMENT,
  `blogContent` text,
  `blogTitle` varchar(200) DEFAULT NULL,
  `blogAuthor` varchar(50) DEFAULT NULL,
  `blogSiteUrl` varchar(200) DEFAULT NULL,
  `blogCreateDate` datetime DEFAULT NULL,
  `blogContentHtml` text,
  PRIMARY KEY (`blogId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
