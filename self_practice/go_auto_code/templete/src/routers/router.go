package routers

import (
	"{{project_name}}/src/routers/api"
	"github.com/gin-gonic/gin"
)

func InitRouter(engine *gin.Engine) {
	api.InitApiGroup(engine)
}
