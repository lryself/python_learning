package routers

import (
	"${{project_name}}/internal/routers/apis"
	"github.com/gin-gonic/gin"
)

func InitRouter(engine *gin.Engine) {
	apis.InitApiGroup(engine)
}
