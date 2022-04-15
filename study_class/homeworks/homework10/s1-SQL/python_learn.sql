/*
Navicat MySQL Data Transfer

Source Server         : my_aliyun
Source Server Version : 80016
Source Host           : rm-2zekx3j75e3rv0k938o.mysql.rds.aliyuncs.com:3306
Source Database       : python_learn

Target Server Type    : MYSQL
Target Server Version : 80016
File Encoding         : 65001

Date: 2020-05-08 15:35:08
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of classes
-- ----------------------------
INSERT INTO `classes` VALUES ('1', '软件1802');
INSERT INTO `classes` VALUES ('2', '软件1801');
INSERT INTO `classes` VALUES ('3', '软件1803');

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT '',
  `age` tinyint(3) unsigned DEFAULT '0',
  `height` decimal(5,2) DEFAULT NULL,
  `gender` enum('男','女','中性','保密') DEFAULT '保密',
  `cls_id` int(10) unsigned DEFAULT '0',
  `is_delete` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('1', '小明', '18', '180.00', '女', '1', '\0');
INSERT INTO `students` VALUES ('2', '小月月', '18', '180.00', '女', '2', '');
INSERT INTO `students` VALUES ('3', '彭于晏', '29', '185.00', '男', '1', '\0');
INSERT INTO `students` VALUES ('4', '刘德华', '59', '175.00', '男', '2', '');
INSERT INTO `students` VALUES ('5', '黄蓉', '38', '160.00', '女', '1', '\0');
INSERT INTO `students` VALUES ('6', '凤姐', '28', '150.00', '保密', '2', '');
INSERT INTO `students` VALUES ('7', '王祖贤', '18', '172.00', '女', '1', '');
INSERT INTO `students` VALUES ('8', '周杰伦', '36', null, '男', '1', '\0');
INSERT INTO `students` VALUES ('9', '程坤', '27', '181.00', '男', '2', '\0');
INSERT INTO `students` VALUES ('10', '刘亦菲', '25', '166.00', '女', '2', '\0');
INSERT INTO `students` VALUES ('11', '金星', '33', '162.00', '中性', '3', '');
INSERT INTO `students` VALUES ('12', '静香', '12', '180.00', '女', '4', '\0');
INSERT INTO `students` VALUES ('13', '郭靖', '12', '170.00', '男', '4', '\0');
INSERT INTO `students` VALUES ('14', '周杰', '34', '176.00', '女', '5', '\0');
