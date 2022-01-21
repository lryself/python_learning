package responseParser

import (
	"registry_center/src/globals/codes"
	"github.com/gin-gonic/gin"
	"net/http"
)

func JsonOK(c *gin.Context, data interface{}) {
	c.JSON(http.StatusOK, gin.H{
		"code":    codes.OK,
		"message": "成功!",
		"data":    data,
	})
}

func JsonParameterIllegal(c *gin.Context, err error) {
	c.JSON(http.StatusOK, gin.H{
		"code":    codes.ParameterIllegal,
		"message": "参数不合法!",
		"err":     err.Error(),
	})
}

func JsonDataError(c *gin.Context, msg string, err error) {
	if msg != "" {
		c.JSON(http.StatusOK, gin.H{
			"code":    codes.DataError,
			"message": "数据错误: " + msg,
			"err":     err.Error(),
		})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"code":    codes.DataError,
			"message": "数据错误！",
			"err":     err.Error(),
		})
	}
}

func JsonInternalError(c *gin.Context, err error) {
	c.JSON(http.StatusOK, gin.H{
		"code":    codes.InternalError,
		"message": "系统错误!",
		"err":     err.Error(),
	})
}

func JsonDBError(c *gin.Context, err error) {
	if err.Error() == "record not found" {
		c.JSON(http.StatusOK, gin.H{
			"code":    codes.NotData,
			"message": "无数据!",
			"err":     err,
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"code":    codes.DBError,
		"message": "数据库错误!",
		"err":     err.Error(),
	})
}
