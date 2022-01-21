package configApis

import (
	"registry_center/src/globals/responseParser"
	"registry_center/src/services"
	"github.com/gin-gonic/gin"
)

type ConfigApiImpl struct {
}

type getParser struct {
	System string `json:"System" binding:"required"`
	Key    string `json:"Key" binding:"required"`
}

func (*ConfigApiImpl) GetHandler(c *gin.Context) {
	var Parser getParser
	var err error
	//解析参数
	err = c.ShouldBindJSON(&Parser)
	if err != nil {
		responseParser.JsonParameterIllegal(c, err)
		return
	}

	var configModel services.SysConfigService
	configModel.System = Parser.System
	configModel.Key = Parser.Key

	err = configModel.Get()
	if err != nil {
		responseParser.JsonDBError(c, err)
		return
	}

	responseParser.JsonOK(c, configModel)
}

type postParser struct {
	System string `json:"System" binding:"required"`
	Key    string `json:"Key" binding:"required"`
	Value  string `json:"Value" binding:"required"`
}

func (*ConfigApiImpl) PostHandler(c *gin.Context) {
	var Parser postParser
	var err error
	//解析参数
	err = c.ShouldBindJSON(&Parser)
	if err != nil {
		responseParser.JsonParameterIllegal(c, err)
		return
	}

	var configModel services.SysConfigService
	configModel.System = Parser.System
	configModel.Key = Parser.Key

	err = configModel.Get()
	if err != nil {
		if err.Error() == "record not found" {
		} else {
			responseParser.JsonDBError(c, err)
			return
		}
	} else {
		responseParser.JsonDataError(c, "已经存在此配置！", err)
		return
	}

	configModel.Value = Parser.Value
	err = configModel.Add()
	if err != nil {
		responseParser.JsonDBError(c, err)
		return
	}

	responseParser.JsonOK(c, configModel)
}

type putParser struct {
	System string `json:"System" binding:"required"`
	Key    string `json:"Key" binding:"required"`
	Value  string `json:"Value" binding:"required"`
}

func (*ConfigApiImpl) PutHandler(c *gin.Context) {
	var Parser putParser
	var err error
	//解析参数
	err = c.ShouldBindJSON(&Parser)
	if err != nil {
		responseParser.JsonParameterIllegal(c, err)
		return
	}

	var configModel services.SysConfigService
	configModel.System = Parser.System
	configModel.Key = Parser.Key

	err = configModel.Update(map[string]interface{}{
		"Value": Parser.Value,
	})
	if err != nil {
		responseParser.JsonDBError(c, err)
		return
	}

	responseParser.JsonOK(c, configModel)
}

type deleteParser struct {
	System string `json:"System" binding:"required"`
	Key    string `json:"Key" binding:"required"`
}

func (*ConfigApiImpl) DeleteHandler(c *gin.Context) {
	var Parser deleteParser
	var err error
	//解析参数
	err = c.ShouldBindJSON(&Parser)
	if err != nil {
		responseParser.JsonParameterIllegal(c, err)
		return
	}

	var configModel services.SysConfigService
	configModel.System = Parser.System
	configModel.Key = Parser.Key

	err = configModel.Delete()
	if err != nil {
		responseParser.JsonDBError(c, err)
		return
	}

	responseParser.JsonOK(c, configModel)
}
