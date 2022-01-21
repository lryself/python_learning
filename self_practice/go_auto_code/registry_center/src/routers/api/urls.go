package api

import (
	"registry_center/src/controller/apis"
	"github.com/gin-gonic/gin"
)

var (
	Api *gin.RouterGroup
)

func InitApiGroup(engine *gin.Engine) {
	Api = engine.Group("api")
	Api.GET("version", apis.GetVersion)
}
