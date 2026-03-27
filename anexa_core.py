def init_deepseek(self):
    """Initialize DeepSeek (Optional)"""
    if not Config.USE_DEEPSEEK:
        self.deepseek_available = False
        logger.info("ℹ️ DeepSeek disabled. Using fallback mode.")
        return
    
    self.deepseek_available = False
    try:
        self.deepseek = DeepSeekEngine(Config.DEEPSEEK_API_KEY)
        self.deepseek_available = self.deepseek.available
        if self.deepseek_available:
            logger.info("✅ DeepSeek ready!")
        else:
            logger.warning("⚠️ DeepSeek not available, using fallback")
    except Exception as e:
        logger.error(f"DeepSeek init failed: {e}")