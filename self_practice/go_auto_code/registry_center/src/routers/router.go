package routers

import (
	"registry_center/src/routers/api"
	"github.com/gin-gonic/gin"
)

func InitRouter(engine *gin.Engine) {
	api.InitApiGroup(engine)
}
